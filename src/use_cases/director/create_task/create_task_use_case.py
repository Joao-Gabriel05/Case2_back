from repositories.task_repository import TaskRepository
from use_cases.director.create_task.create_task_dto import CreateTaskDTO
from fastapi import Request, Response
from entities.task import Task

class CreateTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, create_task_dto: CreateTaskDTO, response: Response, request: Request):
        if (not create_task_dto.status or 
            not create_task_dto.priority or 
            not create_task_dto.title or 
            not create_task_dto.due_date):
            response.status_code = 407
            return {"status": "error", "message": "faltam informações"}

        task = Task(
            status=create_task_dto.status,
            priority=create_task_dto.priority,
            title=create_task_dto.title,
            due_date=create_task_dto.due_date,
        )

        self.task_repository.save(task)
        response.status_code = 201
        return {"status": "success", "message": "Tarefa criada"}
