from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Block(BaseModel):
    id: int
    task_count: int
    generator_id: int
    config: dict

class Template(BaseModel):
    id: int
    name: str
    blocks: List[Block]

class Task(BaseModel):
    id: int
    secret: dict
    question: dict
    answer: dict

class Instance(BaseModel):
    id: int
    name: str
    start: str
    end: str
    duration: str
    status: str
    url: str
    Template: str
    task_count: int
    tasks: List[Task]

# templates = [
#     Template(1, "test 1", [
#         Block(1, 3, 1, {}),
#     ]),
#     Template(2, "test 2", [
#         Block(1, 3, 1, {}),
#     ]),
#     Template(2, "test 2", [
#         Block(1, 3, 1, {}),
#     ])
# ]

# instances = [
#     Instance(1, "Экземпляр 1", "23:23:15 19.04.2023", "00:23:15 20.04.2023", "1:00:00", "Завершен", "1", "Тест 1", 3, [
#         tasks=
#     ])
# ]