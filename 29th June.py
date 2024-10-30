greeting, name="Hello" , "Ayodami"
message=greeting +" "+ name
print(message)

print("Hello", "Alice")
print("Hello" + "Alice")

#This is to differenciate between a tuple and an integer
single_element_tuple = (1,)
print(type(single_element_tuple))

single_element_tuple = (1)
print(type(single_element_tuple))

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
tuple_sum = tuple1 + tuple2
print(tuple_sum)

print(tuple1[0])
print(tuple_sum[-1])

my_tuple = "food","sweet","orange","food" #This is packing
item1, item2, item3, item4 = my_tuple #This is called unpacking
print(my_tuple)
print(item1)
print(item2)
print(item3)
print(f"Food occurs {my_tuple.count("food")} times")
print(my_tuple.index("sweet"))


##This is for practice
school_things = ["Pen", "Biro", "Board", "Tables"]
print(school_things)
school_things.append("Chairs")
print(school_things)


a = 5
b = 7
print(a+b)
print(a*b)
print(b**a)

print(5<3)
print(5**2==25)
