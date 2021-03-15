from flask_restful import Resource
import datetime
import time
from pymongo import MongoClient
from flask_pymongo import PyMongo
from pymongo import mongo_client
from flask import Flask
import logging as logger
import json
from json import JSONEncoder

# json Encoder for datatime


class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


logger.basicConfig(level="DEBUG")


music_app = Flask(__name__)

client = MongoClient(
    "mongodb+srv://Codetemplar99:musicdb1234@musicdb.cigak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.songdb
collection = db["song"]


if __name__ == '__main__':
    logger.debug("Starting Music API")
    from Api import *
    music_app.run(host="0.0.0.0", port="9000",
                  debug=True, use_reloader=True)

logger.basicConfig(level="DEBUG")  # debug on terminal
# create a song


class createSong(Resource):
    def post(self):
        # try:
        song = {"audioFileType": ".mp3", "_id": db.song.find().count() + 1, "audioFileMetadata": {
            "name": "Lost Children.mp3",  "duration": int(400), "uploaded_time":  datetime.datetime.now()}}
        collection.insert_one(song)
        return json.loads(json.dumps(song, indent=4, cls=CustomEncoder))
        # except:
        # print("Internal Server error")


class updateSong(Resource):
    def put(self, songId):
        collection.update_one(filter={'_id': songId}, update={
            '$set': {"audioFileMetadata": {"name": "giant.mp3"}}}, upsert=True)
        sort = {'_id': songId}
        do = collection.find_one(sort)
        return json.loads(json.dumps(do, indent=4, cls=CustomEncoder)), 200

# get song by unique Id


class getSong(Resource):

    def get(self, songId):
        sort = {'_id': songId}
        do = collection.find_one(sort)
        return json.loads(json.dumps(do, indent=4, cls=CustomEncoder)), 200

# delete song by id


class deleteSong(Resource):
    try:
        def delete(self, songId):
            sort = {'_id': songId}
            do = collection.delete_one(sort)
            result = {'result': 'Deleted successfully'}, 200
            return result
    except:
        print("exception occured")
