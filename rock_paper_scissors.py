# rock_paper_scissors.py

import random

def get_computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

def decide_winner(user, computer):
    if user == computer:
        return 'tie'
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return 'win'
    else:
        return 'lose'

def print_scores(user_score, comp_score):
    print(f"\nScore -> You: {user_score} | Computer: {comp_score}\n")

def main():
    print("Welcome to Rock-Paper-Scissors!")
    print("-------------------------------")

    user_score = 0
    comp_score = 0

    while True:
        print("\nChoose one: rock, paper, or scissors")
        user_choice = input("Your choice: ").lower()

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please choose rock, paper, or scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == 'win':
            print("You win this round!")
            user_score += 1
        elif result == 'lose':
            print("You lose this round!")
            comp_score += 1
        else:
            print("It's a tie!")

        print_scores(user_score, comp_score)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
