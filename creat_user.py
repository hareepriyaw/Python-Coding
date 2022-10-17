#CRUD-create (POST), Read (GET), Update(PUT), delete(delete)
import requests
import json


payload={
    "name": "mukesh",
    "job": "automation"
}
resp=requests.post("https://reqres.in/api/users", data=payload)
print(resp.json())
assert resp.json()['job']=='automation'



