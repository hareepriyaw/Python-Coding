# go to httpbin.org. search for get -delayed response-check for its execution and a code is generated after
# 10 sec test. copy that and bring it here.

#this code has to give response in 10sec as per our test in the webpage. but we are giving teh timeout here as 5 sec.
#so, it has to fail. The response is not given in 5 secs.

import requests
resp=requests.get("http://httpbin.org/delay/10",timeout=5)
print(resp.status_code)

#if the timeout in the url is changed to 5 and the variable is set as 10, then the test passes
# as the max timeout is 10sec while we have set to only 5sec. so we will get the response
