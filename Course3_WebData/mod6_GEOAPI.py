import json
import urllib.request, urllib.parse

APIEndpoint = "http://py4e-data.dr-chuck.net/opengeo?"


location = "University of Jaffna"

url = APIEndpoint + urllib.parse.urlencode({'q': location})
print(url)
url = urllib.request.urlopen(url, context = 'ctx')
data = url.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

# print(json.dumps(js, indent=4))
pluscode = js["features"][0]["properties"]["plus_code"]
print(pluscode)