from repositories.task_repository import TaskRepository
from fastapi import Request, Response
from entities.task import Task

class GetTaskByIDUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, task_id: str, response: Response, request: Request):

        task = self.task_repository.get_task_by_id(task_id)
        if not task:
            response.status_code = 407
            return {"status": "error"}
        
        response.status_code = 200
        return task