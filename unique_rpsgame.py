import random

class RPSGame:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]
        self.special_moves = {"fire": "scissors", "water": "rock", "wind": "paper"}
        self.player_score = 0
        self.computer_score = 0
        self.learned_moves = {}

    def get_player_choice(self):
        while True:
            print("Choose: rock, paper, scissors, or type 'special' for a special move.")
            player_choice = input().lower()

            if player_choice in self.choices or player_choice == 'special':
                return player_choice
            else:
                print("Invalid choice. Please choose again.")

    def get_computer_choice(self):
        if not self.learned_moves:
            return random.choice(self.choices)
        else:
            last_player_choice = self.learned_moves["last_player_choice"]
            preferred_choices = self.learned_moves.get(last_player_choice, self.choices)
            return random.choice(preferred_choices)

    def unlock_special_move(self):
        # Add conditions for unlocking special moves
        if self.player_score >= 3:
            return random.choice(list(self.special_moves.keys()))
        return None

    def play_round(self):
        player_choice = self.get_player_choice()

        if player_choice == 'special':
            special_move = self.unlock_special_move()
            if special_move:
                print(f"You unlocked the special move: {special_move}")
                player_choice = special_move
            else:
                print("You haven't unlocked any special moves yet. Choose again.")
                return

        computer_choice = self.get_computer_choice()

        print(f"You chose {player_choice}")
        print(f"Computer chose {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
            self.player_score += 1
        else:
            print("Computer wins!")
            self.computer_score += 1

        self.learned_moves["last_player_choice"] = player_choice

    def play_game(self):
        print("Welcome to Rock, Paper, Scissors!")

        while True:
            self.play_round()
            print(f"Score - You: {self.player_score}, Computer: {self.computer_score}")

            print("Do you want to play again? (yes/no)")
            play_again = input().lower()
            if play_again != 'yes':
                print("Thanks for playing!")
                break

if __name__ == "__main__":
    game = RPSGame()
    game.play_game()
