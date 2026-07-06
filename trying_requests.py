import requests
from bs4 import BeautifulSoup

url="http://google.com"

response=requests.get(url)

print(response.status_code)

html=response.text 

#parsing

soup=BeautifulSoup(html,"html.parser")

print(soup.title.text)

heading=soup.find("h1")

print(heading)
print("--------------------------------------")
links=soup.find_all("a")
for link in links:
	print(link.text)
	print(link["href"])
lsb=soup.find("div",class_="gb_P")

print(lsb.text)

print("********************************")


