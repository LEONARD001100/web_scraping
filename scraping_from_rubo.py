from selenium import webdriver
from selenium.webdriver.common.by import By

#url of rubo
url="https://robu.in/shop/"

#list to store the whole details of robu
details=[]

#opening the chrome
driver=webdriver.Chrome()

#accessing the site
driver.get(url)

featured_categories_items=driver.find_elements(By.CSS_SELECTOR,"div.featured-categories-box")

for category in featured_categories_items:
	category_item=category.find_element(By.CSS_SELECTOR,"div.featured-categorie-title").text
	
	data={
		"title" : category_item
			}
	details.append(data)

driver.quit()

print(details)


