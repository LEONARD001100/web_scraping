import csv

def json_to_csv(listname):
	
	with open("books_details.csv","w",newline="",encoding="utf-8") as files:
		writer=csv.DictWriter(
		files,
		fieldnames=[
			"title",
			"price",
			"availability",
			"rating",
			"product_url",
			"img_url"
			]
		)
		
		writer.writeheader()
		
		writer.writerows(listname)
	
	
