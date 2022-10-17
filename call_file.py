import json
import requests

mydata=open("data_json.py","r").read()

resp=requests.post("https://reqres.in/api/users", data=json.loads(mydata))

print(resp.json())
print(resp.headers.get("Content-Type"))
assert resp.json()['job']=='python developer'

#loads() method deserializes the data into python object
