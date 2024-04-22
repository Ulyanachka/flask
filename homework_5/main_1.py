
'''Необходимо создать API для управления списком задач.
 Каждая задача должна содержать заголовок и описание. 
 Для каждой задачи должна быть возможность указать статус
   (выполнена/не выполнена).

API должен содержать следующие конечные точки:
— GET /tasks — возвращает список всех задач.
— GET /tasks/{id} — возвращает задачу с указанным идентификатором.
— POST /tasks — добавляет новую задачу.
— PUT /tasks/{id} — обновляет задачу с указанным идентификатором.
— DELETE /tasks/{id} — удаляет задачу с указанным идентификатором.

Для каждой конечной точки необходимо проводить валидацию данных запроса 
и ответа. Для этого использовать библиотеку Pydantic'''
from typing import Optional
import logging
from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Api(BaseModel):
    heading: str
    description: Optional[str] = None #не обязательно для заполнения
    status: str
    
@app.get('/tasks')
async def root():
    return {"message": "Hello World"}


@app.get('/tasks/{task_id}')
async def tasks_id(task_id: int, task: str ):
    logger.info('Отработал GET запрос')
    return {'task_id': task_id, 'task': task}


@app.post('/tasks/')
async def create_task(task: Api):
    logger.info('Отработал POST запрос')
    
@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Api):
    logger.info(f'Отработал PUT запрос для task id = {task_id}.')
    return {"task_id": task_id, "task": task}


@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    logger.info(f'Отработал DELETE запрос для item id = {task_id}.')
    return {"task_id": task_id}