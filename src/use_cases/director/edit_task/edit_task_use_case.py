from repositories.task_repository import TaskRepository
from fastapi import Request, Response
from entities.task import Task
from use_cases.director.edit_task.edit_task_dto import EditTaskDTO

class EditTaskUseCase:
    def __init__(self, task_repository: TaskRepository):
        self.task_repository = task_repository

    def execute(self, task_id: str, edit_task_dto: EditTaskDTO, response: Response, request: Request):
        try:
            self.task_repository.update(task_id, edit_task_dto)
            
            response.status_code = 200
            return {"status": "success", "message": "Tarefa atualizada com sucesso"}       
        except ValueError as e:
            response.status_code = 404
            return {"status": "error", "message": str(e)}
        except Exception as e:
            response.status_code = 500
            return {"status": "error", "message": "Erro ao atualizar a tarefa"}
