'''
A simple flask CRUD API
Written by Mitchell Chiadika
In partial fulfilment of the requirements for a developer position
started 14-03-21 
completed 16-03-21 18:44 WAT

'''


# imports
from flask_restful import Resource
from flask_pymongo import PyMongo
from flask import Flask, Response
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
# insatnce of db and collection
db = client.songdb
collection = db["song"]


# Appconfig
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
def createSong():
    try:
        song = {"audioFileType": ".mp3", "_id": db.song.count_documents(filter={}) + 1, "audioFileMetadata": {
            "name": "Lost Children.mp3", "duration": int(400), "uploaded_time": datetime.datetime.now()}}
        collection.insert_one(song)
        return json.loads(json.dumps(song, indent=4, cls=CustomEncoder)), 200
    except:
        return json.loads(json.dumps({"message": "an error occured"}, indent=4, cls=CustomEncoder)), 400


@ music_app.route("/api/mp3/<int:songId>",  methods=["PUT"])
def updateSong(songId):
    collection.update_one(filter={'_id': songId}, update={
        '$set': {"audioFileMetadata": {"name": "Roma.mp3"}}}, upsert=True)
    sort = {'_id': songId}
    do = collection.find_one(sort)
    return json.loads(json.dumps(do, indent=4, cls=CustomEncoder)), 200


# get song by unique Id


@ music_app.route("/api/song/<int:songId>",  methods=["GET"])
def getSong(songId):
    sort = {'_id': songId}
    do = collection.find_one(sort)
    return json.loads(json.dumps(do, indent=4, cls=CustomEncoder)), 200

# delete song by unique id


@ music_app.route("/api/mp3/<int:songId>",  methods=["DELETE"])
def deleteSong(songId):
    sort = {'_id': songId}
    do = collection.delete_one(sort)
    result = {'result': 'Deleted successfully'}, 200
    return result
