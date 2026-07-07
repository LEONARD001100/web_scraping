from selenium import webdriver
from selenium.webdriver.common.by import By
from fastapi import FastAPI

#url of rubo
url="https://robu.in/shop/"

#list to store the whole details of robu
details=[]

#opening the chrome
driver=webdriver.Chrome()

#accessing the site
driver.get(url)

featured_categories_items=driver.find_elements(By.CSS_SELECTOR,"a.featured-categories-item")

for category in featured_categories_items:
	category_item=category.find_element(By.CSS_SELECTOR,"div.featured-categorie-title").text
	
	data={
		"title" : category_item
			}
	details.append(data)

driver.quit()

app=FastAPI()

@app.get("/")
def home():
	return {"message" : "welcome"}

@app.get("/search")
def search(product: str):
	for d in details:
		if product.lower() in d["title"].lower():
			return d
	
	return {"message" : "category not found"}

