#მომხმარებელს უნდა შევეკითხოთ ასაკი, მერე მშობლის და გამოვთვალოთ რამდენი წლით უფროსია მშობელი მასზე 

child_age = int(input("how old are you: "))
mother_age = int(input("how old is your mother: "))
father_age = int(input("how old is your father: "))

print("დედაშენი შენზე " + str(mother_age - child_age) + " წლით დიდია")

print("მამაშენი შენზე " + str(father_age - child_age) + " წლით დიდია")