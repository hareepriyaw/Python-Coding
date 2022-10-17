import requests
resp=requests.get("https://the-internet.herokuapp.com/basic_auth",auth=('hari','priya'))
print(resp.status_code)

#as the credentials are not there present, we will get the response as 401.

#if we can enter the existing credentials, we will get the response as 200