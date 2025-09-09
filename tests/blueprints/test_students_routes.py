def test_students_home_renders(client):
    res = client.get("/")
    assert res.status_code == 200
