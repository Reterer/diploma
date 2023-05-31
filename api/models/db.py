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
    url = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)


def get_instances_by_user(user: User):
    res = session.query(Instance, Template).join(Template).all()
    return list(map(lambda x: x[0], res))


def create_instance(template: Template, instance: Instance):
    pass


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


def create_tasks(user: User, instance_id: int):
    pass


def get_task_list(user: User, instance_id: int):
    pass


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
