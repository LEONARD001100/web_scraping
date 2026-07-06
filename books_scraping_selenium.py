from selenium import webdriver
from selenium.webdriver.common.by import By

#the url to be scraped
url="https://books.toscrape.com"

#list to store all the books
all_book_list=[]

#starting the chrome using selenium

driver=webdriver.Chrome()

driver.get(url)

#scraping the entire books selenium data
books=driver.find_elements(By.CSS_SELECTOR,"article.product_pod")

for book in books:
	title=book.find_element(By.CSS_SELECTOR,"h3 a").get_attribute("title")
	price=book.find_element(By.CSS_SELECTOR,"p.price_color").text
	rating=book.find_element(By.CSS_SELECTOR,"p.star_rating").get_attribute("class")[1]
	availability=book.find_element(By.CSS_SELECTOR,"p.instock availability").text.strip()
	product_url=book.find_element(By.CSS_SELECTOR,"h3 a").get_attribute("href")
	image_url=book.find_element(By.CSS_SELECTOR,"div.image_container a").get_attribute("href")
	
	data={
		"title" : title,
		"price" : price,
		"rating" : rating,
		"availability" : availability,
		"product_url": product_url,
		"image_url" : image_url
		
		}
	all_book_list.append(data)
	

driver.quit()

