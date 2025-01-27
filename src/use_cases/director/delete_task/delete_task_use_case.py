from repositories.task_repository import TaskRepository
from fastapi import Request, Response
from entities.task import Task

class DeleteTaskByIDUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, task_id: str, response: Response, request: Request):

        task = self.task_repository.delete_task(task_id)
        if not task:
            response.status_code = 407
            return {"status": "error"}
        
        response.status_code = 200
        return {"status": "success", "message": "Tarefa excluida"}