import json

student={}

while True:
	
	roll=input("Enter rollno")
	name=input("Enter name")
	age=input("Enter age")
	
	student[roll]={
	"name": name,
	"age": age
		}
	print("Do you want to add more student record y/n?")
	choice=input()
	
	if choice=="n":
		break

with open("student.json","w") as f:
	json.dump(student,f,indent=4)
	
print("data stored succesfully")
	
	
