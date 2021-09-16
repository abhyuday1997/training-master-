from fastapi.testclient import TestClient
from server.app import app
from server.routes.student import router

client = TestClient(router)

data = {
                "fullname": "Bhargava",
                "email": "jdoe@x.edu.ng",
                "course_of_study": "Water resources engineering",
                "year": 2,
                "gpa": 3.0,
            }



def test_insert():
    response = client.post("/",json=data)
    out = response.json()
    message = out['message']
    output = out['data'][0]
    output.pop('id')
    assert response.status_code == 200
    assert message == "Student added successfully."
    assert output == data

def test_get_all():
    response = client.get("/",json=data)
    out = response.json()
    message = out['message']
    output = out['data'][0]
    for x in output:
        del x['id']
    assert response.status_code == 200
    assert message == "Students data retrieved successfully"
    assert data in output

response = client.post("/",json=data)
out = response.json()
id = out['data'][0]['id']

def test_update():
    response = client.put("/{}".format(id),json={ "fullname": "Bhargava Abhyuday",
                "email": "doe@x.edu.ng",
                "course_of_study": "Digital Systems ",
                "year": 4,
                "gpa": 3.0, })     
    assert response.status_code == 200
    out = response.json()
    assert out['message'] == "Student name updated successfully"
