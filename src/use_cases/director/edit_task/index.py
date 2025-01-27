from repositories.task_repository import TaskRepository
from .edit_task_dto import EditTaskDTO
from .edit_task_use_case import EditTaskUseCase
from fastapi import Request, Response, APIRouter

router = APIRouter()

edit_task_use_case = EditTaskUseCase(TaskRepository())
@router.put("/director/edit-task/{task_id}")
def edit_project(task_id: str, edit_task_dto: EditTaskDTO, response: Response, request: Request):
    return edit_task_use_case.execute(task_id, edit_task_dto, response, request)