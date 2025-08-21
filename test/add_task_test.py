import requests

def test_add():
    body = {"title":"generated","completed":False}
    response = requests.post(url="https://todo-app-sky.herokuapp.com/", json=body)
    response_body = response.json()
    
    assert response.status_code == 202
    assert response_body['completed'] == False