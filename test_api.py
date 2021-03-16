from app import music_app

# test for create


def test_Create():
    response = music_app.test_client().post('/api/create')
    assert response.status_code == 200


# test for update
def test_update():
    response = music_app.test_client().put('/api/mp3/1')
    assert response.status_code == 200


# test get by id
def test_getById():
    response = music_app.test_client().get('/api/song/3')
    assert response.status_code == 200

# test delete by Id


def test_delete():
    response = music_app.test_client().delete('/api/mp3/2')
    assert response.status_code == 200
