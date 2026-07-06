with open("data.txt","r+") as f:
	content=f.read()
	f.write("new content")
	f.seek(0)
	new_content=f.read()
print(content)
print("\n-----------------------------\n")
print(new_content)
