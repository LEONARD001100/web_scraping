import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import json
from con_json_to_csv import json_to_csv
import os

#featcing the html
url="https://books.toscrape.com"
headers={
	"User-Agent" : "Mozilla/5.0"
	}
all_books_details=[]
os.makedirs("images",exist_ok=True)
while True:
	print(f"Scraping: {url}")
	response = requests.get(url,headers=headers)
	print(response.status_code)

	#parsing
	html=response.text
	soup=BeautifulSoup(html,"html.parser")

	#scraping the whole details
	books=soup.find_all("article",class_="product_pod")


	#scraping the details of the books


	for book in books:
	
		#scraping the title
		title=book.h3.a.get("title","not found")
		#scraping the price
		price=book.find("p",class_="price_color").text.strip()
		#stock avalilability
		availability=book.find("p",class_="instock availability").text.strip()
		#scraping the rating
		rating=book.find("p",class_="star-rating")["class"][1]
		#scraping the product url
		product_url=urljoin(url,book.h3.a.get("href","not found"))
		#scraping the image url
		img_tag = book.find("img")

		image_url = (urljoin(url,img_tag.get("src", ""))if img_tag else "not found")

		#storing the data 
		data={
			"title":title,
			"price":price,
			"availability":availability,
			"rating":rating,
			"product_url":product_url,
			"image_url":image_url
			}
		all_books_details.append(data)
		#saving the images in a new folder
		if image_url != "not found"
			image_response=requests.get(image_url,headers=headers)
			with open(f"images/book{len(all_books_details)}.jpg","wb") as file:
				file.write(image_response.content)
			print(f"Downloaded image for: {title}")
	#scraping the next link details
	next_button=soup.find("li",class_="next")
	
	if not next_button:
		break

	next_page=next_button.a.get("href","not found")
	url=urljoin(url,next_page)
	

with open("book_details.json","w") as f:
	json.dump(all_books_details,f,indent=4)
print("data stored successfully")

json_to_csv(all_books_details)
print("the csv has been made")



