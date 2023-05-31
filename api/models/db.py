from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import List
from pydantic import BaseModel

# Создаем соединение с базой данных SQLite
engine = create_engine("sqlite:///test.db", echo=True)

# Создаем сессию для взаимодействия с базой данных
Session = sessionmaker(bind=engine)

# Определяем базовую модель
Base = declarative_base()
session = Session()


# Определяем модель User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    full_name = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, nullable=False)

    def __repr__(self):
        return f"<User(username='{self.username}', full_name='{self.full_name}', role='{self.role}')>"


def get_user(username: str):
    return session.query(User).filter(User.username == username).first()


# Определяем модель Templates
class Template(Base):
    __tablename__ = "templates"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)

    def __repr__(self):
        return f"Template(id={self.id}, user_id={self.user_id}, name='{self.name}')"


def get_templates_by_user(user: User):
    return session.query(Template).filter(Template.user_id == user.id).all()


class Generator(Base):
    __tablename__ = "generators"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class InputTemplateTaskBlock(BaseModel):
    name: str
    config: str
    generator_id: int


class TemplateTaskBlock(Base):
    __tablename__ = "templateTaskBlocks"

    id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey("templates.id"))
    generator_id = Column(Integer, ForeignKey("generators.id"))
    name = Column(String, nullable=False)
    block_number = Column(Integer, nullable=False)
    config = Column(String, nullable=False)

    def __repr__(self):
        return f"TemplateTaskBlock(id={self.id}, template_id={self.template_id}, generator_id={self.generator_id}, name={self.name}, block_number={self.block_number}, config={self.config})"


def get_template_blocks_by_template_id(template_id: int):
    return (
        session.query(TemplateTaskBlock)
        .filter(TemplateTaskBlock.template_id == template_id)
        .all()
    )


def create_template_and_task_block(
    user: User, template: Template, template_task_blocks: List[TemplateTaskBlock]
):
    # Нужно закоммитить template, получить его id.
    session.add(template)
    session.commit()
    # print(template)
    # Затем добавить id в blocks и закоммитить их.
    for i in range(len(template_task_blocks)):
        template_task_blocks[i].template_id = template.id
    print(template_task_blocks)
    session.add(*template_task_blocks)
    session.commit()
    # Затем готово
    print(template_task_blocks)
    pass


# Определяем модель Instances
class Instance(Base):
    __tablename__ = "instances"

    id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey("templates.id"))
    name = Column(String, nullable=False)
    url = Column(String)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)


def get_instances_by_user(user: User):
    res = (
        session.query(Instance, Template)
        .join(Template)
        .filter(Template.user_id == user.id)
        .all()
    )
    return list(map(lambda x: x[0], res))


def create_instance(instance: Instance):
    session.add(instance)
    session.commit()


# Определяем модель InstanceTasks
class InstanceTask(Base):
    __tablename__ = "instanceTasks"

    id = Column(Integer, primary_key=True)
    instance_id = Column(Integer, ForeignKey("instances.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    template_task_block_id = Column(Integer, ForeignKey("templateTaskBlocks.id"))
    number = Column(Integer, nullable=False)
    public_data = Column(String, nullable=False)
    secret_data = Column(String, nullable=False)
    answer_data = Column(String, nullable=False)


from datetime import datetime


class Test(BaseModel):
    id: int
    name: str
    start_time: datetime
    end_time: datetime


# test_id == instance_id Ну или пока так
def get_test(instance_id: int):
    info = session.query(Instance).filter(Instance.id == instance_id).first()
    return Test(
        id=info.id, name=info.name, start_time=info.start_time, end_time=info.end_time
    )


import generators
import json


def generate_tasks(block: TemplateTaskBlock):
    # Как это происходит. У нас есть список генераторов.
    gen = generators.GENERATOR_LIST[block.generator_id]
    # Парсинг текстового json в dict
    config = json.loads(block.config)
    # Непосредственно сама генерация задач
    public, secret = gen.generate_tasks(config)

    return public, secret


# TODO может быть потом переместить от сюда функцию
def create_tasks(user: User, instance_id: int):
    # Самая важная функция..
    # Мы попадаем сюда, если у пользователя нет задач
    instance = session.query(Instance).filter(Instance.id == instance_id).first()
    # Нужно найти блоки задач
    blokcs = get_template_blocks_by_template_id(instance.template_id)
    # Нужно сгенерировать задачи
    instance_tasks = []
    num = 0
    for block in blokcs:
        public, secret = generate_tasks(block)
        # Заполнение полей
        tasks = [
            InstanceTask(
                instance_id=instance_id,
                user_id=user.id,
                template_task_block_id=block.id,
                number=num + i,
                public_data=json.dumps(public[i]),
                secret_data=json.dumps(secret[i]),
                answer_data="{}",
            )
            for i in range(len(public))
        ]
        num += len(tasks)
        instance_tasks.extend(tasks)
    # Закоммитить их
    session.add(*instance_tasks)
    session.commit()
    # Фсе
    pass


def get_task_block_list(user: User, instance_id: int):
    res = (
        session.query(InstanceTask, TemplateTaskBlock)
        .join(TemplateTaskBlock)
        .filter(
            InstanceTask.user_id == user.id and InstanceTask.instance_id == instance_id
        )
        .all()
    )
    return res


def add_answer_task(user: User, instance_id: int, instance_task_id: int, answer: str):
    pass


# # Создаем таблицу в базе данных
# Base.metadata.create_all(engine)

# # Добавление пользователей в сессию
# session.add(
#     User(
#         username="admin",
#         hashed_password="admin",
#         role="admin",
#         full_name="Тестовый Аккаунт Преподавателя",
#     )
# )
# session.add(
#     User(username="test1", hashed_password="test", role="student", full_name="Тест 1")
# )
# session.add(
#     User(username="test2", hashed_password="test", role="student", full_name="Тест 2")
# )
# # Фиксация изменений в базе данных
# session.commit()
