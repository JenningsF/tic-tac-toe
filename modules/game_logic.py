import random

class Game:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2

    # Assigns player markers based on Player 1's selection
    def marker_select(self):
        marker_selection = "INVALID"
        acceptable_markers = ['X','O']
        
        # Loop until correct input is given
        while marker_selection not in acceptable_markers:
            marker_selection = input("\nPlayer 1, select your marker (X or O): ")

            if marker_selection not in acceptable_markers:
                print("Invalid marker selection")
            else:
                self.player1.marker = marker_selection
                if marker_selection == 'X':
                    self.player2.marker = 'O'
                elif marker_selection == 'O':
                    self.player2.marker = 'X'

    # Randomly decides which player goes first
    def choose_first(self):
        return random.randint(1,2)

    # Switches who's turn it is
    def switch_players(self, turn):
        next_turn = 0

        if turn == 1:
            next_turn = 2
            return next_turn
        elif turn == 2:
            next_turn = 1
            return next_turn
        else:
            print("ERROR: Something went wrong in switching players!\n")

    def turn(self, turn, board, player1, player2):
            # Display board
            print(board)

            if turn == player1.player_number:
                selected_position = player1.take_turn(board)
                board.place_marker(player1.marker, selected_position)
            elif turn == player2.player_number:
                selected_position = player2.take_turn(board)
                board.place_marker(player2.marker, selected_position)
            else:
                print("ERROR: Something went wrong when taking a turn\n")

    def round(self):
        # Players select X or O markers
        self.marker_select()

        # Choose random player to go first
        turn = self.choose_first()

        is_game_over = False

        while not(is_game_over):
            self.turn(turn, self.board, self.player1, self.player2)

            is_game_over = self.board.win_check()

            # If there's not a stalemate or no one has won, then next player switches
            if not(is_game_over):
                turn = self.switch_players(turn)

            # Checks if board is full and in a stalemate
            if not(self.board.full_board_check()):
                print(self.board)
                print("\nThe cat's got it! It's a stalemate, try again\n")
                break


        if is_game_over:
            print(self.board)
            if turn == self.player1.player_number:
                print(f"\nPlayer {self.player1.player_number} wins!\n")
            elif turn == self.player2.player_number:
                if self.player2.is_human:
                    print(f"\nPlayer {self.player2.player_number} wins!\n")
                elif not(self.player2.is_human):
                    print("Computer wins!\n")