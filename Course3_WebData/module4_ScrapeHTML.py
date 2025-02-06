from bs4 import BeautifulSoup
import requests

targetURL = 'https://py4e-data.dr-chuck.net/comments_2076244.html'

# Load the page
page = requests.get(targetURL)
# Parse the page
soup = BeautifulSoup(page.content, 'html.parser')

#Find the numbers
numbers = soup.find_all('span', class_='comments')

total = 0
for number in numbers:
    number = int(number.text)
    total +=  number
print(total)
