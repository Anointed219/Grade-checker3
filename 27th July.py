Gender = input("Gender: ").title()

match Gender:
    case "Male":
        print("Good day Sir")
    case "Female":
        print("Good day Ma")
    case _:
        print("Nothing like that")

Day = input("Day: ").title()

match Day:
    case "Monday":
        print("Get to work")
    case "Saturday" | "Sunday":
        print("Weekend")
    case _:
        print("Weekday")

a, b, operation = 5, 6, input("Enter Operation: ")

match operation:
    case "add":
        print(a + b)
    case "subtract":
        print(a - b)
    case "multiply":
        print(a * b)
    case "divide":
        print(a / b)
    case _:
        print("Unknown opeartion")

        

        