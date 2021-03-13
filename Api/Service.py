from flask_restful import Resource
import logging as logger


class getSong(Resource):

    def get(self, songId):
        return {
            "Id": "songID={}".format(songId), "Name": "Billie Jeans.mp3", "Duration": 240, "Uploaded_time": "28/03/21",
        }, 200


class createSong(Resource):

    def post(self):
        return {
            "audioFileType": "mp3",
            "audioFileMetaData": {
                "Name": "Billie Jeans.mp3", "Duration": "240", "Uploaded_time": "28/03/21"}
        }, 200


class updateSong(Resource):

    def put(self, songId):
        return {
            "audioFileType": "mp3",
            "audioFileMetaData": {
                "Id": "{}".format(songId), "Name": "Billie Jeans_instrumental.mp3", "Duration": "320",
                "Uploaded_time": "30/03/21"}
        }, 200


class deleteSong(Resource):
    def delete(self, songId):
        return {
            "deleted": "songID={}".format(songId)
        }, 200
