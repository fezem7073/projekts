score = 0

answer1 = input("What is 2 + 2? ")
if answer1 == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

answer2 = input("What color is grass? ")
if answer2 == "green":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print(f"You got {score} out of 2!")