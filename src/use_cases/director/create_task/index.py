from repositories.task_repository import TaskRepository
from .create_task_dto import CreateTaskDTO
from .create_task_use_case import CreateTaskUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

create_task_use_case = CreateTaskUseCase(TaskRepository())

@router.post("/director/create-task")
def create_task(create_task_dto:CreateTaskDTO, response:Response, request:Request):
    return create_task_use_case.execute(create_task_dto, response, request)

