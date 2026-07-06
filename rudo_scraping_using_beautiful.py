#importing the dependancies
import requests
from bs4 import BeautifulSoup


url="https://robu.in/shop/"						#the url of rudo

category_list=[]						#the list to store the dara

#fetching the html
headers={"User-Agent" : "Mozilla/5.0"}					#the header for tricking the site

print("Scraping")

responce=requests.get(url,headers=headers)

print(responce.status_code)						#checking status

html=responce.text							#fetching the whole site to get the html

soup=BeautifulSoup(html,"html.parser")					#parsing to get the html part only

categories=soup.find_all("a",class_="featured-categories-item")

#scraping the category names

for cat in categories:
	category_title=cat.find("div",class_="featured-categorie-title").text
	
	data={"title" : category_title}
	
	category_list.append(data)

print(len(category_list))






