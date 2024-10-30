my_list =["pen", "pencil", "eraser"]
print(my_list)
my_list.append("book")
print(my_list)
my_list2 = ["Ayomide", "Dami", "Ayodami"]
print(my_list2)
my_list2.extend(["Roberts","Folorunso"])
print(my_list2)
my_list2.remove("Dami")
print(my_list2)
my_list3 = ["Book", "Pen", "Biro", "Textbook"]
print(my_list3)
my_list3.insert(3,"Pencil")
print(my_list3)
my_list3.pop()
print(my_list3)
my_list3.pop(2)
print(my_list3)
my_list4 = ["School", "Office", "House"]
What = my_list4.index("Office")
print(What)
what = my_list4.append("Later")
print(what)
my_list5 = ["Apple", "Banana", "Apple", "Strawberry"]
hello = my_list5.count("Apple")
print(hello)
matrix = [[1,2,3],[4,5,6],[6,7,8]]
print(matrix[0][0])
print(matrix[1][2])
numbers = [[1,2,3,4],[4,5,6,7],[7,8,9,0],[0,1,2,3]]
print(numbers[2][3])

age = 18
if age >= 18:
	print("You're old")
	print("Why are you old")

age = 18
if age >= 18:
	print("You are an adult")
else:
	print("You aren't an adult")
if age <= 18:
	print("You are an adult")
if age < 18:
	print("You are an adult")
else: 
	print("You aren't an adult")


age = 13
if age := 13:## It can also be age == 13
	print("You're a teenager")
elif age < 13:
	print("You're a child")
else:
	print("You're an adult")
