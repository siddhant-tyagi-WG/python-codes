import requests
import re
from bs4 import BeautifulSoup

search_query = input("Enter what you want to google")
url = f'https://www.google.com/search?q={search_query}'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
num=10
links = soup.findAll("a")
cnt=1
for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
    print(cnt,end=" ")
    print(re.split(":(?=http)", link["href"].replace("/url?q=", "")))
    cnt=cnt+1
    num=num-1
    if(num==0):
        break

