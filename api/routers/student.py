from fastapi import APIRouter
import models.db as db
from pydantic import BaseModel
from typing import List

router = APIRouter(
    prefix="/student",
    tags=["student"],
)

# AUTH ----------------------------------
# TODO нужно сделать норм авторизацию
user = db.get_user("test1")

# TESTING -------------------------------


# Выводит информацию о тесте
class GetTest(BaseModel):
    class Task(BaseModel):
        id: int
        generator_id: int
        short_name: str
        public_data: dict

    test: db.Test
    items: List[Task]


import json


@router.get("/test/{test_id}", response_model=GetTest)
async def get_test(test_id: str):
    # Получение информации о тесте
    test = db.get_test(test_id)
    # Получение списка задач
    res = db.get_task_block_list(user, test_id)
    # Если список задач для данного пользователя пустой, то создать его
    if len(res) == 0:
        db.create_tasks(user, test_id)
        res = db.get_task_block_list(user, test_id)

    # Оставим только нужную информацию
    items = [
        GetTest.Task(
            id=task.id,
            generator_id=block.generator_id,
            short_name=task.number,
            public_data=json.loads(task.public_data),
        )
        for (task, block) in res
    ]
    return GetTest(test=test, items=items)


@router.get("/test/{test_id}/{task_id}")
async def get_task(test_id: str, task_id: str):
    # Получение описания задачи
    return {}


@router.put("/test/{test_id}/{task_id}")
async def put_task(test_id: str, task_id: str):
    # Сохранение ответа на задачу
    return {}
