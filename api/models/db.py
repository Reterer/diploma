from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

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
