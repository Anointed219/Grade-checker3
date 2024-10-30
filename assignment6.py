import sys

name = input("What's your name? ")
maths = int(input("Input your Mathematics score: "))
english = int(input("Input your English score: "))
science = int(input("Input your Science score: "))

if maths > 100 or english > 100 or science > 100:
      print("Error, One or more of your score is above 100, Please try again")
      sys.exit()

if maths >= 90:
      math_grade = "A"
elif maths >= 80:
      math_grade = "B"
elif maths >= 70:
      math_grade = "C"
elif maths >= 60:
      math_grade = "D"
elif maths >= 50:
      math_grade = "E"
elif maths <50:
      math_grade = "F"
      
if english >= 90:
      english_grade = "A"
elif english >= 80:
      english_grade = "B"
elif english >= 70:
      english_grade = "C"
elif english >= 60:
      english_grade = "D"
elif english >= 50:
      english_grade = "E"
elif english <50:
      english_grade = "F"   
      
if science >= 90:
      science_grade = "A"
elif science >= 80:
      science_grade = "B"
elif science >= 70:
      science_grade = "C"
elif science >= 60:
      science_grade = "D"
elif science >= 50:
      science_grade = "E"
elif science <50:
      science_grade = "F"       
      
print(f"Hi {name}, Here are your grades and your final result: \nSUBJECT\tSCORE\tGRADE\nMATHS\t{maths}\t{math_grade}\nENGLISH\t{english}\t{english_grade}\nSCIENCE\t{science}\t{science_grade}")

average = (maths + english + science)/3
print(f"Your average score is {average}")

if average >= 90:
      average_grade = "A"
elif average >= 80:
      average_grade = "B"
elif average >= 70:
      average_grade = "C"
elif average >= 60:
      average_grade = "D"
elif average >= 50:
      average_grade = "E"
elif average <50:
      average_grade = "F"
      
print(f"Your average grade is {average_grade}")