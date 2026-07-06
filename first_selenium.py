from selenium import webdriver

from selenium.webdriver.common.by import By

print("Starting")

driver = webdriver.Chrome()
url="https://books.toscrape.com"
print("Started")

driver.get(url)

books=driver.find_elements(
		By.CLASS_NAME,
		"product_pod"		
		)

print(books[1].find_element(By.TAG_NAME,"h3").find_element(By.TAG_NAME,"a").get_attribute("title"))



driver.quit()
