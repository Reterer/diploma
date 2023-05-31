from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
import models.db as db


router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)

# AUTH ----------------------------------


# TEMPLATES -----------------------------
user = db.get_user("admin")


@router.get("/templates")
async def get_templates():
    # Получение списка шаблонов
    templates = db.get_templates_by_user(user)
    return templates


class PostTemplate(BaseModel):
    class TaskBlock(BaseModel):
        name: str
        generator_id: int
        block_number: int
        config: str

    name: str
    blocks: List[TaskBlock]


@router.post("/templates")
async def post_template(post_template: PostTemplate):
    # Создание нового шаблона
    # Суть в том, что бы для пользователя user создать новый шаблон
    # 1. Получаем данные в формате postTemplates
    # 2. Нужно распарсить его. Заполнить данные для db
    # 2.1 template
    # 2.2 TemplateTaskBlocks - имя, номер блока, настройки и id генератора
    # 3. Отправить

    template = db.Template(
        user_id=user.id,
        name=post_template.name,
    )
    blokcs = []
    for i in range(len(post_template.blocks)):
        blokcs.append(
            db.TemplateTaskBlock(
                generator_id=post_template.blocks[i].generator_id,
                name=post_template.blocks[i].name,
                block_number=i,
                config=post_template.blocks[i].config,
            )
        )
    db.create_template_and_task_block(user, template, blokcs)
    return {}


class TemplateBlock(BaseModel):
    id: int
    template_id: int
    generator_id: int
    name: str
    block_number: int
    config: str


@router.get("/templates/{template_id}", response_model=List[TemplateBlock])
async def get_templates_id(template_id: int):
    # Получение блоков заданий
    blokcs = db.get_template_blocks_by_template_id(template_id)
    blokcs = [TemplateBlock(**block.__dict__) for block in blokcs]
    return blokcs


# TODO Нужно вообще по хорошему дополнить API отдельными методами для каждого болка
@router.put("/templates/{template_id}")
async def put_templates_id(template_id: int):
    # Обновление шаблона
    return {}


@router.delete("/templates/{template_id}")
async def delete_templates_id(template_id: int):
    # удаление шаблона
    return {}


# INSTANCES -----------------------------


@router.get("/instances")
async def get_instances():
    # Получить список экземпляров тестов
    return {}


@router.post("/instances")
async def post_instances():
    # Создание нового экземпляра
    return {}


@router.delete("/instances/{instance_id}")
async def delete_instances_id(instance_id: str):
    # Удалить экземпляр
    return {}


@router.get("/instances/{instance_id}/table")
async def get_instances_id_table(instance_id: str):
    # Получить таблицу?
    return {}


@router.get("/instances/{instance_id}/data")
async def get_instances_id_data(instance_id: str):
    # Получить данные?
    return {}


# GENERATOR -----------------------------


@router.get("/generators")
async def get_generators():
    # Получить список генераторов
    return {}


@router.post("/generators")
async def post_generators():
    # загрузить новый генератор
    return {}


@router.delete("/generators/{generator_id}")
async def delete_generators_id(generator_id: str):
    # загрузить новый генератор
    return {}
