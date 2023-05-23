from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    username = Column(String)
    hashedPassword = Column(String)
    role = Column(String)

class TemplateTaskBlock(Base):
    __tablename__ = 'template_task_blocks'

    id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey('templates.id'))
    generator_id = Column(Integer, ForeignKey('generators.id'))
    task_count = Column(Integer)
    settings_json = Column(JSONB)

    template = relationship("Template", backref="template_task_blocks")
    generator = relationship("Generator", backref="template_task_blocks")

class Generator(Base):
    __tablename__ = 'generators'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Template(Base):
    __tablename__ = 'templates'

    id = Column(Integer, primary_key=True)
    name = Column(String)

class Instance(Base):
    __tablename__ = 'instances'

    id = Column(Integer, primary_key=True)
    template_id = Column(Integer, ForeignKey('templates.id'))
    name = Column(String)
    start_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP)

    template = relationship("Template", backref="instances")

class InstanceTask(Base):
    __tablename__ = 'instance_tasks'

    id = Column(Integer, primary_key=True)
    instance_id = Column(Integer, ForeignKey('instances.id'))
    user_id = Column(Integer, ForeignKey('users.id'))
    task_number = Column(Integer)
    task_data = Column(JSONB)
    user_answer = Column(JSONB)

    instance = relationship("Instance", backref="instance_tasks")
    user = relationship("User", backref="instance_tasks")


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Строка подключения к базе данных PostgreSQL
# Замените значения <your_host>, <your_database>, <your_user>, <your_password> на фактические данные для вашей базы данных
connection_string = 'postgresql://postgres:05130222@localhost/test'

# Создание движка SQLAlchemy для подключения к базе данных
engine = create_engine(connection_string)

# Создание сессии SQLAlchemy
Session = sessionmaker(bind=engine)
session = Session()

# Теперь вы можете использовать объект session для выполнения операций с базой данных

# Пример: добавление нового пользователя в таблицу "Users"
new_user = User(fullname='John Doe', username='johndoe', hashedPassword='123456', role='user')
session.add(new_user)
session.commit()

# Пример: получение всех пользователей из таблицы "Users"
users = session.query(User).all()
for user in users:
    print(user.fullname)

# Закрытие сессии
session.close()