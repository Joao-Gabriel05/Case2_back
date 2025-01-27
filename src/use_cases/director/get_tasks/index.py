from repositories.task_repository import TaskRepository
from .get_task_use_case_by_id import GetTaskByIDUseCase
from fastapi import Request, Response, APIRouter
from .get_task_use_case import GetTaskUseCase

router = APIRouter()

get_task_by_id_use_case = GetTaskByIDUseCase(TaskRepository())
get_task_use_case= GetTaskUseCase(TaskRepository())


@router.get("/director/get-task/{task_id}")
def get_task_by_id(task_id: str ,response:Response, request:Request):
    return get_task_by_id_use_case.execute(task_id,response, request)

@router.get("/director/get-task")
def get_task(response:Response, request:Request):
    return get_task_use_case.execute(response, request)
