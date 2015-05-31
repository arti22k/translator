import http.client
import urllib.parse
import ssl
import json

params = urllib.parse.urlencode({'scope':'http://api.microsofttranslator.com', 'grant_type':'client_credentials', 'client_id': 'MyNewAppClientID', 'client_secret': 'gLjhrvCBArFwt9gFSUkrzBvqhjP4QvWgOuv/0I3w6bY='})
headers = {"Content-type": "application/x-www-form-urlencoded"}
conn = http.client.HTTPSConnection('datamarket.accesscontrol.windows.net')
conn.set_debuglevel(10)
conn.request("POST", "/v2/OAuth2-13", params, headers)
response = conn.getresponse()
data = response.read()
conn.close()
print('data ==>  ')
print(data)

access_token = json.loads(data.decode("utf-8"))['access_token']
print('\r\n' + 'access_token  =>  ')
print(urllib.parse.unquote(access_token))
headers2 = {'Authorization': 'Bearer ' + access_token}
params2 = urllib.parse.urlencode({'text':'hello', 'to':'pl', 'from':'en'})
# params2 = {}
conn2 = http.client.HTTPConnection('api.microsofttranslator.com')
conn2.set_debuglevel(10)
conn2.request("POST", "/V2/Http.svc/Translate", params2, headers2)
response2 = conn2.getresponse()
data2 = response2.read()
conn2.close()
print('\r\n' + 'data2 ==> ')
print(data2)
