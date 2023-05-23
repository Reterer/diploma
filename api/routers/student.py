from fastapi import APIRouter

router = APIRouter(
    prefix="/student",
    tags=["student"],
)

# AUTH ----------------------------------

# TESTING -------------------------------

@router.get("/test/{test_id}")
async def get_test(test_id: str):
    # Получение списка задач
    return {}

@router.get("/test/{test_id}/{task_id}")
async def get_task(test_id: str, task_id: str):
    # Получение описания задачи
    return {}

@router.put("/test/{test_id}/{task_id}")    
async def put_task(test_id: str, task_id: str):
    # Сохранение ответа на задачу
    return {}