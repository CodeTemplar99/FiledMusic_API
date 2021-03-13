from flask_restful import Api
from app import flaskAppInstance
from .Service import getSong, createSong, updateSong, deleteSong

restserver = Api(flaskAppInstance)
# get song route
restserver.add_resource(getSong, "/api/service/getSong/<string:songId>")

# create song route
restserver.add_resource(createSong, "/api/service/create/<string:songId>")


# update song route
restserver.add_resource(updateSong, "/api/service/mp3/<string:songId>")


# delete song route
restserver.add_resource(deleteSong, "/api/service/delete/mp3/<string:songId>")
