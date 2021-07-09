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

# Asks if player wants to play against another player or computer player
def opponent_choice():
    choice = "INVALID"
    acceptable_choices = ['1','2']
    human_player = False

    # Loop until correct input is given
    while choice not in acceptable_choices:
        print("\n1: Human Player")
        print("2: Computer Player")
        choice = input("What opponent would you like to face? ")

        if choice not in acceptable_choices:
            print("Invalid input")

        if choice == '1':
            human_player = True
        elif choice == '2':
            human_player = False

    return human_player

# Display board
def display_board(board):
    index = 0

    # Clear console before displaying board
    # os.system("cls")
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
def choose_first(human_player):
    if human_player:
        return random.randint(1,2)
    elif not(human_player):
        return 1

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

# Generates computer's move
def get_computer_move(current_board, markers):
    # Contains all columns,rows, and diagonals that win with three of a kind
    win_conditions = {"column1":[1,4,7], "column2":[2,5,8], "column3":[3,6,9],
                        "row1":[7,8,9], "row2":[4,5,6], "row3":[1,2,3],
                        "diagonal1":[7,5,3], "diagonal2":[1,5,9]}
    corners = [1,3,7,9]

    # # Iterate through current game board and it's win conditions
    # for n in win_conditions.values():
    #     print(n)
    #     try:
    #         # Choose center position if it is open
    #         if current_board[5] == ' ':
    #             return 5
    #         # Check if open move can win the game
    #         elif [current_board[n[0]],current_board[n[1]],current_board[n[2]]].count(markers[1]) == 2:
    #             move = [current_board[n[0]],current_board[n[1]],current_board[n[2]]].index(' ')
    #             print("1st elif")
    #             print(move)
    #             return move
    #         # Check if open move can block and prevent opponent from winning
    #         elif [current_board[n[0]],current_board[n[1]],current_board[n[2]]].count(markers[0]) == 2:
    #             move = [current_board[n[0]],current_board[n[1]],current_board[n[2]]].index(' ')
    #             print("2d elif")
    #             print(move)
    #             return move
    #         # else:
    #         #     while True:
    #         #         move = random.randint(1,9)
    #         #         if current_board[move] == ' ':
    #         #             print("Random")
    #         #             return move
    #         #             break
    #     except ValueError:
    #         pass

    # First Column Check
    if (current_board[7] == current_board[4] == markers[1]) and current_board[1]== ' ':
        return 1
    if (current_board[7] == current_board[1] == markers[1]) and current_board[4]== ' ':
        return 4
    if (current_board[4] == current_board[1] == markers[1]) and current_board[7]== ' ':
        return 7

    # Second Column Check
    if (current_board[8] == current_board[5] == markers[1]) and current_board[2]== ' ':
        return 2
    if (current_board[8] == current_board[2] == markers[1]) and current_board[5]== ' ':
        return 5
    if (current_board[5] == current_board[2] == markers[1]) and current_board[8]== ' ':
        return 8

    # Third Column Check
    if (current_board[9] == current_board[6] == markers[1]) and current_board[3]== ' ':
        return 3
    if (current_board[9] == current_board[3] == markers[1]) and current_board[6]== ' ':
        return 6
    if (current_board[6] == current_board[3] == markers[1]) and current_board[9]== ' ':
        return 9

    # First Row Check
    if (current_board[7] == current_board[8] == markers[1]) and current_board[9]== ' ':
        return 9
    if (current_board[7] == current_board[9] == markers[1]) and current_board[8]== ' ':
        return 8
    if (current_board[8] == current_board[9] == markers[1]) and current_board[7]== ' ':
        return 7

    # Second Row Check
    if (current_board[4] == current_board[5] == markers[1]) and current_board[6]== ' ':
        return 6
    if (current_board[4] == current_board[6] == markers[1]) and current_board[5]== ' ':
        return 5
    if (current_board[5] == current_board[6] == markers[1]) and current_board[4]== ' ':
        return 4

    # Third Row Check
    if (current_board[1] == current_board[2] == markers[1]) and current_board[3]== ' ':
        return 3
    if (current_board[1] == current_board[3] == markers[1]) and current_board[2]== ' ':
        return 2
    if (current_board[2] == current_board[3] == markers[1]) and current_board[1]== ' ':
        return 1

    # Forward Diagonal Check
    if (current_board[1] == current_board[5] == markers[1]) and current_board[9]== ' ':
        return 9
    if (current_board[1] == current_board[9] == markers[1]) and current_board[5]== ' ':
        return 5
    if (current_board[5] == current_board[9] == markers[1]) and current_board[1]== ' ':
        return 1

    # Backward Diagonal Check
    if (current_board[7] == current_board[5] == markers[1]) and current_board[3]== ' ':
        return 3
    if (current_board[7] == current_board[3] == markers[1]) and current_board[5]== ' ':
        return 5
    if (current_board[5] == current_board[3] == markers[1]) and current_board[7]== ' ':
        return 7

    else:
        while True:
            move = random.randint(1,9)
            if current_board[move] == ' ':
                return move
                break

# Ask player for next position (1-9) and checks if it's open
def player_choice(board, turn, human_opponent, markers):
    free_position = False

    # Player 1 chooses next move
    if turn == 1:
        print(f"\nPlayer {turn}'s turn!")
        while free_position == False:
            position_choice = player_input()
            free_position = space_check(board, position_choice)

            if free_position == False:
                print(f"Position {position_choice} is already taken!")
    # Player 2 chooses next move
    elif turn == 2:
        # Player 2 is Human Opponent
        if human_opponent:
            print(f"\nPlayer {turn}'s turn!")

            while free_position == False:
                position_choice = player_input()
                free_position = space_check(board, position_choice)

                if free_position == False:
                    print(f"Position {position_choice} is already taken!")
        # Player 2 is Computer Opponent
        elif not(human_opponent):
            position_choice = get_computer_move(board, markers)

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

        human_player = opponent_choice()

        # Player 1 selects X or O
        player_markers = marker_select()

        # Choose random player to go first
        player_turn = choose_first(human_player)

        while player_win == False:
            # Display board
            display_board(game_board)

            # Player chooses play position
            marker_position = player_choice(game_board, player_turn, human_player, player_markers)

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
                print("\nThe cat's got it! It's a stalemate, try again\n")
                break

    print("\nThank you for playing Tic-tac-toe!\n")

# Run full game
run_game()
