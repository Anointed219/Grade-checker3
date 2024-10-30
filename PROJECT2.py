import random

name = input("Enter your name: ")
values = ("Rock", "Paper", "Scissors")
rounds = ("1", "3", "5")
selected_round = input("==> ")
selected_round_index = rounds.index(selected_round)
print(selected_round_index)

game = (("ROUND 1\n" + name + ": " + random.choice(values) + "\nComputer: " + random.choice(values)), 
        ("ROUND 1\n" + name + ": " + random.choice(values) + "\nComputer: " + random.choice(values) + "\nROUND 2\n" + name + ": " + random.choice(values) + "\nComputer: " + random.choice(values) + "\nROUND 3\n" + name + ": " + random.choice(values) + "\nComputer: " + random.choice(values)),
        ("ROUND 1\n" + name + ": " + random.choice(values) + "\nComputer: " + random.choice(values) + "\nROUND 2\n" + name + ": " + random.choice(values) + "\nComputer: " + random.choice(values) + "\nROUND 3\n" + name + ": " + random.choice(values) + "\nComputer: " + random.choice(values) + "\nROUND 4\n" + name + ": " + random.choice(values) + "\nComputer: " + random.choice(values) + "\nROUND 5\n"  + name + ": " + random.choice(values) + "\nComputer: " + random.choice(values)),
        ("ROUND 1\nROUND 2\nROUND 3\nROUND 4\nROUND 5"))
print(game[selected_round_index])