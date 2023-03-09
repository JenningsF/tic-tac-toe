import time
import random

class Player:
    def __init__(self, number):
        self.marker = ''
        self.is_human = True
        self.player_number = number

    def is_valid_position(self, position):
        acceptable_range = range(1,10)

        if position in acceptable_range:
            return True
        else:
            return False

        
class HumanPlayer(Player):
    def __init__(self, number):
        self.marker = ''
        self.is_human = True
        self.player_number = number
    
    # Take player's input and returns position to place marker as 'X' or 'O'
    # Checks if input is a digit and if it is a valid position
    def player_input(self):
        choice = ''

        # Loop until correct input is given
        while not(choice.isdigit()) or not(self.is_valid_position(choice)):
            choice = input("Please choose a position (1-9): ")

            if choice.isdigit() and self.is_valid_position(int(choice)):
                break
            # Check if input is a digit
            elif not(choice.isdigit()):
                print("Input is not a number")
            # Check if input is a valid position on the board
            elif not(self.is_valid_position(int(choice))):
                print("Input is not in acceptable range")
            else:
                print("ERROR: Something went wrong with your input")
            
        return int(choice)
    
    # Ask player for next position (1-9) and checks if it's open
    def take_turn(self, board):
        free_position = False

        print(f"\nPlayer {self.player_number}'s turn!")

        # Loop continues until available position is selected
        while not(free_position):
            position_choice = self.player_input()
            free_position = board.is_open_position(position_choice)

            # Prints message if position not available
            if not(free_position):
                print(f"Position {position_choice} is already taken!")

        return position_choice

class ComputerPlayer(Player):
    def __init__(self, number):
        self.marker = ''
        self.is_human = False
        self.player_number = number

    # Simulates computer player making a deciding
    def thinking(self):
        print("\nThinking", end='')
        for num in range(1,4):
            print('.', end='', flush=True)
            time.sleep(1)

    # Generates computer's move
    def get_computer_move(self, current_board):
        # Contains all columns,rows, and diagonals that win with three of a kind
        win_conditions = {"column1":[1,4,7], "column2":[2,5,8], "column3":[3,6,9],
                            "row1":[7,8,9], "row2":[4,5,6], "row3":[1,2,3],
                            "diagonal1":[7,5,3], "diagonal2":[1,5,9]}
        # corners = [1,3,7,9]

        # Assigns markers
        if self.marker == 'X':
            opponent_marker = 'O'
        elif self.marker == 'O':
            opponent_marker = 'X'
        
        
        position_choice = 0
        
        # Choose center position if it is open
        if current_board.board[5] == ' ':
            position_choice = 5
            print(f"Computer Selected move: {position_choice}")
            return position_choice

        # Check for winning moves or blocking moves
        else:
            # Iterate through win_conditions and check if open move can win the game
            for n in win_conditions.values():
                try:
                    if [current_board.board[n[0]],current_board.board[n[1]],current_board.board[n[2]]].count(self.marker) == 2:
                        position_choice = n[[current_board.board[n[0]],current_board.board[n[1]],current_board.board[n[2]]].index(' ')]
                        print(f"Computer Selected move: {position_choice}")
                        return position_choice
                except ValueError:
                    continue

            # Iterate through win_conditions and check if open move can block opponent from winning
            for n in win_conditions.values():
                try:
                    if [current_board.board[n[0]],current_board.board[n[1]],current_board.board[n[2]]].count(opponent_marker) == 2:
                        position_choice = n[[current_board.board[n[0]],current_board.board[n[1]],current_board.board[n[2]]].index(' ')]
                        print(f"Computer Selected move: {position_choice}")
                        return position_choice
                except ValueError:
                    continue

        # If center spot is taken and there are no winning or blocking moves, select random open space
        while True:
            position_choice = random.randint(1,9)
            if current_board.board[position_choice] == ' ':
                print(f"Computer Selected move: {position_choice}")
                return position_choice
                break

    def take_turn(self, board):
        free_position = False

        print(f"\nPlayer {self.player_number}'s turn!")

        # Loop continues until available position is selected
        while free_position == False:
            self.thinking()
            position_choice = self.get_computer_move(board)
            free_position = board.is_open_position(position_choice)

            # Prints message if position not available
            if not(free_position):
                print(f"Position {position_choice} is already taken!")

        return position_choice
