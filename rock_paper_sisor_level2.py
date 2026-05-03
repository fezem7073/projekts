import random

choices = ["rock", "paper", "scissors"]

player_score = 0
computer_score = 0
rounds = 0

while rounds < 3:
    player = input("Choose rock, paper or scissors (or 'quit' to stop): ")
    
    if player == "quit":
        break
    
    if player not in choices:
        print("Invalid choice! Try again.")
        continue
    
    computer = random.choice(choices)
    print("Computer chose:", computer)

    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "scissors":
        print("You win this round!")
        player_score += 1
    elif player == "paper" and computer == "rock":
        print("You win this round!")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1
    
    rounds += 1
    print(f"Score - You: {player_score} | Computer: {computer_score}\n")

print("Game over!")
if player_score > computer_score:
    print("You won the game!")
elif computer_score > player_score:
    print("Computer won the game!")
else:
    print("It's a tie!")