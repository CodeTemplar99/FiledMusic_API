# from flask_restful import Resource
# import logging as logger


# class createSong(Resource):

#     def post(self):
#         song = {"audioFileType": ".mp3", "audioFileMetadata": {"_id": db.song.find().count() + 1, "name": "lost children.mp3",  "duration": int(
#             300), "uploaded_time":  datetime.datetime.utcnow()}}, 200
#         curTime = datetime.datetime.now()
#         curTime = int(time.mktime(curTime.timetuple()))

#         collection.insert_one(song)
#         return song, 200


# class updateSong(Resource):

#     def put(self, songId):
#         return {
#             "audioFileType": "mp3",
#             "audioFileMetaData": {
#                 "Id": "{}".format(songId), "Name": "Billie Jeans_instrumental.mp3", "Duration": "320",
#                 "Uploaded_time": "30/03/21"}
#         }, 200


# class getSong(Resource):

#     def get(self, songId):
#         return {
#             "Id": "songID={}".format(songId), "Name": "Billie Jeans.mp3", "Duration": 240, "Uploaded_time": "28/03/21",
#         }, 200


# class deleteSong(Resource):
#     def delete(self, songId):
#         return {
#             "deleted": "songID={}".format(songId)
#         }, 200


# # cluster = MongoClient(
# #     "mongodb+srv://Codetemplar99:musicdb1234@musicdb.cigak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# # db = cluster["songdb"]
# # collection = db["song"]
