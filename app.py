# imports
from flask_restful import Resource
from flask_pymongo import PyMongo
from flask import Flask, Response
from pymongo import mongo_client
from pymongo import MongoClient
from json import JSONEncoder
import logging as logger
import datetime
import time
import json


# flask instance
music_app = Flask(__name__)


# MongoDb client
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


# json Encoder for datatime
class CustomEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime.date, datetime.datetime)):
            return obj.isoformat()


# create a song
@music_app.route("/api/create",  methods=["POST"])
def post():
    # try:
    song = {"audioFileType": ".mp3", "_id": db.song.find().count() + 1, "audioFileMetadata": {
        "name": "Lost Children.mp3",  "duration": int(400), "uploaded_time":  datetime.datetime.now()}}
    collection.insert_one(song)
    return json.loads(json.dumps(song, indent=4, cls=CustomEncoder))


@music_app.route("/api/mp3/<int:songId>",  methods=["PUT"])
def put(songId):
    collection.update_one(filter={'_id': songId}, update={
        '$set': {"audioFileMetadata": {"name": "giant.mp3"}}}, upsert=True)
    sort = {'_id': songId}
    do = collection.find_one(sort)
    return json.loads(json.dumps(do, indent=4, cls=CustomEncoder)), 200

# get song by unique Id


@music_app.route("/api/song/<int:songId>",  methods=["GET"])
def get(songId):
    sort = {'_id': songId}
    do = collection.find_one(sort)
    return json.loads(json.dumps(do, indent=4, cls=CustomEncoder)), 200

# delete song by id


@music_app.route("/api/mp3/<int:songId>",  methods=["DELETE"])
def delete(songId):
    sort = {'_id': songId}
    do = collection.delete_one(sort)
    result = {'result': 'Deleted successfully'}, 200
    return result
