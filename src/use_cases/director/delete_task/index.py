from repositories.task_repository import TaskRepository
from .delete_task_use_case import DeleteTaskByIDUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()
delete_task_use_case = DeleteTaskByIDUseCase(TaskRepository())
@router.delete("/director/delete-task/{task_id}")
def delete_task(task_id:str,response:Response, request:Request):
    return delete_task_use_case.execute(task_id,response, request)
