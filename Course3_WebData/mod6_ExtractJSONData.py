import json
import urllib.request

# #Test inputs
# targetURL = 'http://py4e-data.dr-chuck.net/comments_42.json' #Sample (Sum=2553)
targetURL = 'http://py4e-data.dr-chuck.net/comments_2076247.json' # Actual (Sum ends with 98)

# Load the page
response = urllib.request.urlopen(targetURL)
JSON_data = json.loads(response.read().decode())

total = 0
for item in JSON_data['comments']:
    value = item['count']
    total += int(value)
    print(value)

print(f"Total: {total}")
