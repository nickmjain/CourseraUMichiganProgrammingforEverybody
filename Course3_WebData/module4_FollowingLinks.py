from bs4 import BeautifulSoup
import requests

#Example inputs
# targetURL = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html' # Example
# linkPos = 3
# numRepeat = 4

# #Test inputs
targetURL = 'http://py4e-data.dr-chuck.net/known_by_Alani.html' #test
linkPos = 18
numRepeat = 7

print(targetURL)
for i in range(numRepeat):
    # Load the page
    page = requests.get(targetURL)
    # Parse the page
    soup = BeautifulSoup(page.content, 'html.parser')

    #get list of all HREF tags with anchor element a
    allLinkTags = soup.find_all('a')
    targetURL = allLinkTags[linkPos-1].get('href')
    print(targetURL)

targetName = allLinkTags[linkPos-1].get_text()
print(targetName)