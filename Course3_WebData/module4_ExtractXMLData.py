from bs4 import BeautifulSoup
import requests
import urllib.request

# #Test inputs
# targetURL = 'https://py4e-data.dr-chuck.net/comments_42.xml' #sample
targetURL = 'http://py4e-data.dr-chuck.net/comments_2076246.xml' #actual

# Load the page
response = urllib.request.urlopen(targetURL)
xml_data = BeautifulSoup(response.read(), features = 'xml')

#find all values in comment.count in the XML tree
commentCounts = xml_data.select('comment > count')

total = 0;
for count in commentCounts:
    count = int(count.text)
    total += count

print(total)

