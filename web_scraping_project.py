import requests
import re
from bs4 import BeautifulSoup

search_query = input("Enter what you want to google")
url = f'https://www.google.com/search?q={search_query}'
page = requests.get(url)
soup = BeautifulSoup(page.content,'html.parser')
num=100
links = soup.findAll("a")
cnt=1
k=1
while(num!=0):
    for link in soup.find_all("a", href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        print(cnt, end=" ")
        print(re.split(":(?=http)", link["href"].replace("/url?q=", "")))
        cnt = cnt + 1
        num = num - 1
        if (num == 0):
            break
    if(num==0):
        break
    elif(num!=0):
        k=int(k)
        k=k+1
        k=str(k)
        url=f'https://www.google.com/search?q={search_query}/page'+k
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')