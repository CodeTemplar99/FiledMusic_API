from flask_restful import Api
from app import music_app
from app import getSong, createSong, updateSong, deleteSong

restserver = Api(music_app)
# get song route
restserver.add_resource(getSong, "/api/song/<int:songId>")

# create song route
restserver.add_resource(createSong, "/api/create")


# update song route
restserver.add_resource(updateSong, "/api/mp3/<int:songId>")


# delete song route
restserver.add_resource(deleteSong, "/api/mp3/<int:songId>")
