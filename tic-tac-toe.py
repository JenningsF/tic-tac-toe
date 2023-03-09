#*****************************************************************
#
#                    Two-player Tic-Tac-Toe
#
#*****************************************************************


import os
import game_logic
import gameboard
import player

# Display game header
def display_header():
    print("""
======================================================================================================================

                                                  WELCOME TO
 _________  ___  ________               _________  ________  ________               _________  ________  _______
|\___   ___\\\  \|\   ____\             |\___   ___\\\   __  \|\   ____\             |\___   ___\\\   __  \|\  ___ \\
\|___ \  \_\ \  \ \  \___|  ___________\|___ \  \_\ \  \|\  \ \  \___|  ___________\|___ \  \_\ \  \|\  \ \   __/|
     \ \  \ \ \  \ \  \    |\____________\  \ \  \ \ \   __  \ \  \    |\____________\  \ \  \ \ \  \\\\\  \ \  \_|/__
      \ \  \ \ \  \ \  \___\|____________|   \ \  \ \ \  \ \  \ \  \___\|____________|   \ \  \ \ \  \\\\\  \ \  \_|\ \\
       \ \__\ \ \__\ \_______\                \ \__\ \ \__\ \__\ \_______\                \ \__\ \ \_______\ \_______\\
        \|__|  \|__|\|_______|                 \|__|  \|__|\|__|\|_______|                 \|__|  \|_______|\|_______|

======================================================================================================================

    """)

# Display game instructions
def display_instructions():
    print("The game board will correspond to a standard numpad:\n")
    print("7 | 8 | 9")
    print("---------")
    print("4 | 5 | 6")
    print("---------")
    print("1 | 2 | 3\n")

# Asks if players want to play again and return bool
def replay(): 
    choice = "INVALID"
    acceptable_choices = ['y',"yes",'n',"no"]
    continue_game = False

    # Loop until correct input is given
    while choice not in acceptable_choices:
        choice = input("Are you ready to play? (Yes or No): ")
        choice = choice.lower()

        if choice not in acceptable_choices:
            print("Invalid input")

        if choice == 'y' or choice == "yes":
            continue_game = True
        elif choice == 'n' or choice == "no":
            continue_game = False

    return continue_game

# Asks if player wants to play against another player or computer player
def choose_human_opponent():
    choice = "INVALID"
    acceptable_choices = ['1','2']
    human_opponent = False

    # Loop until correct input is given
    while choice not in acceptable_choices:
        print("\n1: Human Player")
        print("2: Computer Player")
        choice = input("What opponent would you like to face? ")

        if choice not in acceptable_choices:
            print("Invalid input")

        if choice == '1':
            human_opponent = True
        elif choice == '2':
            human_opponent = False

    return human_opponent

# Run Game
def play():
    # Clear console when game runs
    os.system("cls")

    # Print game header once
    display_header()

    # Print instructions (num pad) once
    display_instructions()

    # Check ready to play OR continue to play
    while replay():
        game_board = gameboard.GameBoard()

        # Asks for human or computer opponent
        is_human_opponent = choose_human_opponent()

        player1 = player.HumanPlayer(1)
        if(is_human_opponent):
            player2 = player.HumanPlayer(2)
        elif not(is_human_opponent):
            player2 = player.ComputerPlayer(2)

        game = game_logic.Game(game_board, player1, player2)

        game.round()

    # When game is finished, print message and exit
    print("\nThank you for playing Tic-tac-toe!\n")

# Run full game
play()
