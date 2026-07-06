hospital_details={}
hospitals=[]
while True:
	
	hospital_name=input("Enter the name of the hospital :")
	while True:
		try:
			hospital_rating=float(input("Enter the rating :"))
			break
		except ValueError:
			print("Enter a valid rating")
	hospital_location=input("Enter the location of the hospital :")
	
	hospital_details[hospital_name]={
	"hospital" : hospital_name,
	"hospital_rating" : hospital_rating,
	"location" : hospital_location}
	
	hospitals.append(hospital_name)
	
	print("Do you want to add more y/n :")
	choice=input("Enter your choice :")
	if choice.lower()=="n":
		break
print(hospitals)
print("\n------------------------\n")
print(hospital_details)


search_choice=input("Do you want to search any hospital y/n :")
if search_choice.lower()=="y":
	name_of_hospital=input("Enter the name of the hospital to find:")
	found=False
	for key in hospital_details:
		if key.lower()==name_of_hospital.lower():
			print("Hospital found")
			print(hospital_details[key])
			found=True
			break
	if not found:
		print("Hospital not found")

print("Thank you")
