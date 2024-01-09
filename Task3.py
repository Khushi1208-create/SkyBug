'''User Input: Prompt the user to choose rock, paper, or scissors. 
Computer Selection: Generate a random choice (rock, paper, or scissors) for the computer. 
Game Logic: Determine the winner based on the user's choice and the computer's choice. Rock beats 
scissors, scissors beat paper, and paper beats rock. 
Display Result: Show the user's choice and the computer's choice. Display the result, whether the user wins, 
loses, or it's a tie. 
Score Tracking (Optional): Keep track of the user's and computer's scores for multiple rounds. 
Play Again: Ask the user if they want to play another round. 
User Interface: Design a user-friendly interface with clear instructions and feedback.'''
import random
def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
    return user_choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou chose {user_choice}.")
        print(f"Computer chose {computer_choice}.\n")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    play_game()
