#In PUT- all the attributes of the object have to be given while sending the request.
# If the record does not exist, it should create.
# If it exists, it should update.
{ 'name':'hari','phone':34456,'address':'ghjhh 9886'}

#In PATCH - specify the attributes that have to be updated.
{'address':'kjhkjklj 56789'}

import requests
import json


payload={
    "name": "morpheus",
  #  "job": "zion resident"
}
#resp=requests.put("https://reqres.in/api/users/2", data=payload)
#resp=requests.post("https://reqres.in/api/register", data=payload)
resp=requests.patch("https://reqres.in/api/users/2", data=payload)
print(resp)
print(resp.json())
#assert resp.json()['token']=="QpwL5tke4Pnpja7X4"
#assert resp.json()['job']=="zion resident"
assert resp.json()['name']=="morpheus"