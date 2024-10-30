#This program is to generate a password using string slicing
name =input("Enter your name: ")
year =input("Enter your year of birth: ")

print(name[:3] + str(year[:2]))
print(name[3:] + str(year[2:]))
print(name[:5] + str(year[2:]))
print(name[:2] + str(year[:3]))

#OR
name =input("Enter your name: ")
year =input("Enter your year of birth: ")

print(name[:3] + str(year[:2]), name[3:] + str(year[2:]),name[:5] + str(year[2:]),name[:2] + str(year[:3]))
