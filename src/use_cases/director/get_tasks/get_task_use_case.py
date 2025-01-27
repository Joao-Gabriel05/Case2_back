from repositories.task_repository import TaskRepository
from use_cases.director.create_task.create_task_dto import CreateTaskDTO
from fastapi import Request, Response
from entities.task import Task

class GetTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, response: Response, request: Request):

        tasks = self.task_repository.get_all_tasks()
        if not tasks:
            response.status_code = 204
            return {"status": "success", "message": "Nenhuma tarefa encontrada"}
        
        response.status_code = 200
        return tasks