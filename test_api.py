from app import music_app
from app import getSong, createSong, updateSong, deleteSong
# import pytest


def test_hello():
    response = music_app.test_client().get('/api/create')

    assert response.status_code == 200
    # assert response.data == b'Hello, World!'
