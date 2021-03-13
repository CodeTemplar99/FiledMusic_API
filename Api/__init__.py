from flask_restful import Api
from app import flaskAppInstance
from .Task import Task

restserver = Api(flaskAppInstance)

restserver.add_resource(Task, "/api/task")
restserver.add_resource(TaskById, "/api/task/id/<String:TaskId>")
