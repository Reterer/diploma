from fastapi import APIRouter
# import ..mock
router = APIRouter(
    prefix="/admin",
    tags=["admin"],
)

# AUTH ----------------------------------
# TODO

# TEMPLATES -----------------------------

@router.get("/templates")
async def get_templates():
    # Получение списка шаблонов
    return {}

@router.post("/templates")
async def post_templates():
    # Создание нового шаблона
    return {}

@router.put("/templates/{template_id}")
async def put_templates_id(template_id: str):
    # Обновление шаблона
    return {}

@router.delete("/templates/{template_id}")
async def delete_templates_id(template_id: str):
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

