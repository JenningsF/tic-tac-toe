#*****************************************************************
#
#                    Two-player Tic-Tac-Toe
#
#*****************************************************************

import random
import os

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


# Display board
def display_board(board):
    index = 0

    # Clear console before displaying board
    os.system("cls")
    # Iteratres through array for printing
    print("\n")
    for num in range(1,len(board)):
        if num < 4:
            index = num + 6
            print(board[index], end = " ")
        elif num > 6:
            index = num - 6
            print(board[index], end = " ")
        else:
            print(board[num], end = " ")

        if num % 3 != 0:
            print("|", end = " ")
        if num < 9 and num % 3 == 0:
            print("\n----------")
    print("\n")

# Takes player input and assign marker as 'X' or 'O'.
def player_input():
    choice = "INVALID"
    acceptable_range = range(1,10)
    within_range = False

    # Loop until correct input is given
    while choice.isdigit() == False or within_range == False:
        choice = input("Please choose a position (1-9): ")

        # Check if input is a digit
        if choice.isdigit() == False:
            print("Input is not a number")

        # Check if input is within range
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                print("Input is not in acceptable range")
                within_range = False
    return int(choice)

# Take board, marker ('X' or 'O') and position number and assigns it to the board
def place_marker(board, marker, position):
    board[position] = marker

# Checks if a player has won after marker is placed
def win_check(board, marker):
    player_wins = False

    # Vertical Checks
    if board[7] == board[4] == board[1] == marker:
        player_wins = True
    elif board[8] == board[5] == board[2] == marker:
        player_wins = True
    elif board[9] == board[6] == board[3] == marker:
        player_wins = True

    # Horizontal Checks
    if board[7] == board[8] == board[9] == marker:
        player_wins = True
    elif board[4] == board[5] == board[6] == marker:
        player_wins = True
    elif board[1] == board[2] == board[3] == marker:
        player_wins = True

    # Diagonal Checks
    if board[7] == board[5] == board[3] == marker:
        player_wins = True
    elif board[9] == board[5] == board[1] == marker:
        player_wins = True

    return player_wins

# Randomly decide first player
def choose_first():
    return random.randint(1,2)

# Returns player markers based on Player 1's selection
def marker_select():
    marker_selection = "INVALID"
    markers = ["#","",""]
    acceptable_markers = ['X','O']

    # Loop until correct input is given
    while marker_selection not in acceptable_markers:
        marker_selection = input("\nPlayer 1, select your marker (X or O): ")

        if marker_selection not in acceptable_markers:
            print("Invalid marker selection")

        if marker_selection == 'X':
            markers[1] = marker_selection
            markers[2] = 'O'
        elif marker_selection == 'O':
            markers[1] = marker_selection
            markers[2] = 'X'
    return markers

# Returns whether selected space is available
def space_check(board, position):
    return board[position] == " "

# Checks if board is full
def full_board_check(board):
    return ' ' in board

# Ask player for next position (1-9) and checks if it's open
def player_choice(board, turn, markers):
    free_position = False

    print(f"\nPlayer {turn}'s turn!")
    while free_position == False:
        position_choice = player_input()
        free_position = space_check(board, position_choice)

        if free_position == False:
            print(f"Position {position_choice} is already taken!")

    return position_choice

# Switches who's turn it is
def switch_players(turn):
    next_turn = 0

    if turn == 1:
        next_turn = 2
        return next_turn
    elif turn == 2:
        next_turn = 1
        return next_turn
    else:
        print("ERROR: switch_players()\n")

# Run Game
def run_game():
    # completed_games = 0
    player_turn = 0
    marker_position = 0

    # Clear console when game runs
    os.system("cls")

    # Print game header once
    display_header()

    # Print instructions (num pad) once
    display_instructions()

    # Check ready to play OR continue to play
    while replay():
        player_win = False
        game_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        player_markers = ['#','','']

        # Player 1 selects X or O
        player_markers = marker_select()

        # Choose random player to go first
        player_turn = choose_first()

        while player_win == False:
            # Display board
            display_board(game_board)

            # Player chooses play position
            marker_position = player_choice(game_board, player_turn, player_markers)

            # Place Marker
            place_marker(game_board, player_markers[player_turn], marker_position)

            # Check if a player has won
            player_win = win_check(game_board, player_markers[player_turn])

            # If there's not a stalemate or no one has won, then next player switches
            if player_win == False:
                player_turn = switch_players(player_turn)
            elif player_win == True:
                display_board(game_board)
                print(f"\nPlayer {player_turn} wins!\n")
                break

            # Checks if board is full and in a stalemate
            if not(full_board_check(game_board)):
                display_board(game_board)
                print("\nIt's a stalemate! Try again\n")
                break

    print("\nThank you for playing Tic-tac-toe!\n")

# Run full game
run_game()
