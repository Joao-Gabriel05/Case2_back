import os
from typing import List
from mongoengine import *
from cryptography.fernet import Fernet
from entities.task import Task
from models.task_model import TaskModel
from models.fields.sensivity_field import SensivityField

class TaskRepository:
    fernet = Fernet(os.getenv("FERNET_SECRET_KEY"))

    def save(self, task: Task) -> None:
        task_model = TaskModel()
        task_dict = task.model_dump()

        for k in TaskModel.get_normal_fields():
            if k not in task_dict:
                continue

            task_model[k] = task_dict[k]

        for k in TaskModel.sensivity_fields:
            task_model[k] = SensivityField(fernet=self.fernet, data=task_dict[k])

        task_model.save()
        return None

    def get_task_by_id(self, task_id: str) -> dict:
        task = TaskModel.objects.with_id(task_id)
        if not task:
            return None
        task_dict = task.to_mongo().to_dict()
        task_dict['_id'] = str(task_dict['_id'])
        return task_dict

    def update(self, task_id: str, updated_data: dict) -> None:
        task = TaskModel.objects.with_id(task_id)
        updated_data = updated_data.model_dump()
        if not task:
            raise ValueError("Tarefa não encontrada")
        for key, value in updated_data.items():
            if hasattr(task, key):
                setattr(task, key, value)

        task.save()

    def get_all_tasks(self) -> List[dict]:
        tasks = TaskModel.objects()
        result = []

        for task in tasks:
            task_dict = task.to_mongo().to_dict()
            task_dict['_id'] = str(task_dict['_id']) 
            result.append(task_dict)

        return result

    def delete_task(self, task_id: str) -> bool:
        task = TaskModel.objects.with_id(task_id)
        if not task:
            return False
        task.delete()
        return True