from flask_restful import Resource
import logging as logger


class Task(Resource):

    def get(self):
        logger.debug("inside get method")
        return{"message": "in get method"}, 200

    def post(self):
        logger.debug("inside post method")
        return{"message": "in post method"}, 200

    def update(self):
        logger.debug("inside update method")
        return{"message": "in update method"}, 200

    def delete(self):
        logger.debug("inside delete method")
        return{"message": "in delete method"}, 200
