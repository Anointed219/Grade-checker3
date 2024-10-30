int_list = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", 3.14, [5, 6, 7]]

print(mixed_list[3])
print(int_list[1:3])
print(fruits[0:2])
print(fruits[:2])
print(mixed_list[2:])
print(int_list[-3:])
print(int_list[2:])
print(int_list[:3])

#This is practicing
colours = ["red", "blue", "green", "yellow", "purple", "black"]
numbers = [2, 4, 6, 8, 3, 12, 67]
mixed_list = ["white", "orange", [2,6,7], 3.56]

print(colours[4])
print(mixed_list[:2])

int_list = [1, 2, 3, 4, 5]
fruit = ["apple", "banana", "cherry"]
mixed_list = [1, "hello", 3.14, [5, 6, 7]]

fruit[1] = "mango"
print(fruit)

fruit[fruit.index("cherry")] = "banana"
print(fruit)


##This is 20th July
age = str(input("Enter your age: "))
if age >= str(18):
    print("You are an adult")
if age != str(18):
    print("You are still a child")

##Continuation of 20th July
##This was done on online python interpreter 
age = int(input("How old are you?: "))

if age <= 17 and age >= 13:
    print("You're a teenager")
elif age < 13:
    print("You're a child")
else:
    print("You're an adult")


age = int(input("How old are you?: "))

if age <= 16 and age >= 13:
    print("You're a teenager")
elif age < 13:
    print("You're a child")
elif age == 17:
    print("You're almost an adult")
else:
    print("You're an adult")


##Classwork for 20th July
name =input("What is your name?: ")

maths = int(input("What's your score in maths?: "))
english = int(input("What's your score in english?: "))
science = int(input("What's your score in science?: "))

average = (maths + english + science)/3
if average >= 50:
    print(f"Hey {name}, You passed. Congrats")
elif average <= 50:
    print(f"Hey {name}, Sorry  but you failed")





