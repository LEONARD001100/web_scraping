from selenium import webdriver
from selenium.webdriver.commom.by import By

url="https://books.toscrape.com/"

all_books_details=[]


drivers=webdriver.Chrome()

driver.get(url)

books=find_elements(
	By.CSS_SELECTOR,
	"article.product_pod"	
		)

for book in books:
	
	book_name=books.find_element(By.CSS_SELECTOR,"h3 a")get_attribute("title")
	book_price=books.find_element(By.CSS_SELECTOR,"div.product_price p").text
	book_rating=books.find_element(By.CSS_SELECTOR,"p.star_rating")get_attribute("class")[1]
	book_avalilabality=books.find_element(By.CSS_SELECTOR,"p.availability").text
	book_img=books.find_elemenr(By.CSS_SELECTOR,"div.image_container a img")get_attribute("src")
	
	book_url=url+book_img
	
	data={
		"title" : book_name,
		"price" : book_price,
		"rating" : book_rating,
		"availability" : book_availability,
		"image_url" : book_img
		
		}
	all_book_list.append(data)

driver.quit()
