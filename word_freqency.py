
count={}

with open("data.txt","r") as f:
	for line in f:
		content=line.lower().split()
		
		for word in content:
	
			if word in count:
				count[word]+=1
			else:
				count[word]=1
		
		
print(count)
		
