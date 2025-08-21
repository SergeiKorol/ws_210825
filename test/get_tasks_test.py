import requests

def get_tasks_test():
    response = requests.get("https://todo-app-sky.herokuapp.com/")
    assert response.status_code == 200
    assert type(response.json()) is list


def get_tasks_test1():
    response = requests.get("https://todo-app-sky.herokuapp.com/")
    assert response.status_code == 200
    assert type(response.json()) is list