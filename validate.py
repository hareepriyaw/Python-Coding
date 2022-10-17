import requests

res=requests.get("https://reqres.in/api/users?page=2")
json_res=res.json()
print(json_res)
#print(json_res['total_pages'])
#print(json_res['total'])
#assert json_res['total_pages']==2
#assert json_res['total']==3, "does not match"
#look for the json data in the online json viewer to capture the individual values to be used in this program.
#print(json_res["data"][0]["email"])
#assert json_res["data"][0]["email"].endswith("reqres.in"), "does not match the mentioned value"
#print(json_res['data'][2]['last_name'])
#assert json_res['data'][2]['last_name']!=None
#print(json_res['support']['url'])
