import time

def main():
    print("Welcome to Tic-Tac-Toe!\n")
    # Create a game instance from the TicTacToe module
    game = TicTacToe()
    # Start the game and handle game repetition within this method
    game.play_game()

class TicTacToe:
    def __init__(self):
        """
        Initializes the Tic-Tac-Toe game with default settings.
        Sets up the board dimensions, winning conditions, delay, symbols, players, and player choice tracking.
        """
        self.board_rows, self.board_columns = 3, 3  # Board dimensions
        self.WINNING_CONDITIONS = (
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        )
        self.game_delay = 2  # Delay after each move in seconds, set to 0 for no delay
        self.player_symbols = ('-', 'X', 'O')  # Symbols for empty, Player 1, and Player 2
        self.total_players = 2  # Number of players in the game
        self.player_choices = [[0] * 9, [0] * 9]  # Tracking each player's moves as a 1D list
        self.colors = {'-': '\033[90m', 'X': '\033[94m', 'O': '\033[91m'}  # ANSI color codes for symbols

    def show_position(self, row_index, column_index, columns=3):
        '''Converts row and column into a linear index for the game board'''
        return row_index * columns + column_index

    def get_player_mark(self, cell_index):
        """
        Determines the mark ('-', 'X', or 'O') for a given cell index based on player choices.
        
        - param cell_index: The index of the cell in the player_choices lists
        - return - The symbol representing the player mark for the cell
        """
        if self.player_choices[0][cell_index] == 1:
            return 'X'
        elif self.player_choices[1][cell_index] == 1:
            return 'O'
        else:
            return '-'

    def show_board(self):
        """
        Creates and returns a string representation of the current state of the game board.
        Uses get_player_mark to determine the symbol to display for each cell.
        
        - return - A string visualizing the game board with current player moves.
        """
        game_board = ''

        # Iterate over each row to build the board representation
        for row in range(self.board_rows):
            row_cells = []

            # Iterate over each column in the current row
            for col in range(self.board_columns):
                # Get the linear index for the current cell
                cell_index = self.show_position(row, col)
                mark = self.get_player_mark(cell_index)
                # Get the corresponding color code for the mark
                color_code = self.colors.get(mark, '\033[0m')  # Default to no color if not found
                # Append the colored mark to the row's cells list
                row_cells.append(f"{color_code}{mark}\033[0m")

            # Join the row's cells with vertical bars and append to the board string
            game_board += ' | '.join(row_cells) + '\n'
        return game_board

    def check_for_winner(self):
        """
        Checks the current game state to see if any player has won.
        
        - return - True if a winning condition is met by any player, otherwise False.
        """
        for condition in self.WINNING_CONDITIONS:
            for player_num in range(self.total_players):
                winner = True  # Start with the assumption that the player has won
                for loci in condition:
                    if self.player_choices[player_num][loci] != 1:
                        winner = False  # Mark player as not winning
                        break 
                if winner:  # If winner is still True, then all positions are marked by the player
                    return True
        return False  # If no winning conditions met, return False
    
    # At game restart reset player_choices lists for tracking each player's moves
    def reset_game(self):
        self.player_choices = [[0] * 9, [0] * 9]

    def play_game(self):

        """
        Begins and controls the main game loop. It handles the alternating turns between players,
        validates each move, and checks the game state for a win or a draw after each move.
        After a game concludes, it prompts the players to either start a new game or exit.
        """
        
        # Loop to allow for consecutive games without restarting the program.
        while True:
            # Resets the game to the initial state for a new game.
            self.reset_game()
            # Prints the initial state of the game board.
            print()
            print(self.show_board())

            # Main game loop for the turns, assuming a maximum of 9 turns in a 3x3 grid.
            for turn in range(9):
                # Determines the current player based on the turn count.
                current_player = turn % self.total_players

                # Loop to get a valid move from the current player.
                valid_choice = False
                while not valid_choice:

                    move_choice = input(f"\n\033[33mPlayer {current_player + 1} ({self.player_symbols[current_player + 1]})\033[0m, enter your move (1-9): ")

                    # Check if the input is a digit and within the valid range
                    if not move_choice.isdigit() or not 1 <= int(move_choice) <= 9:
                        print("\nInvalid move. Please enter a number between 1 and 9.")
                        continue

                    # Convert the move from string to integer and adjust for zero indexing.
                    move_number = int(move_choice) - 1
                    
                    if self.player_choices[0][move_number] != 0 or self.player_choices[1][move_number] != 0:
                        print("\nThat cell is already taken. Please choose another.")
                        continue # Asks for input again if the cell is taken.
                    # Move is valid; mark the cell and exit the loop to proceed to the next player's turn.
                    valid_choice = True
                    self.player_choices[current_player][move_number] = 1
                    print()
                    print(self.show_board())
                # Check if the current player has won after their move.
                if self.check_for_winner():
                    print(f"\033[33m{self.player_symbols[current_player + 1]:>10}\033[32m wins the game!\033[0m\n")
                    break
                 # After all moves are made and no winner, declare a draw.
                if turn == 8:
                    draw = "It's a draw!"
                    print(f"\033[35m{draw:>20}\033[0m\n")
                    break

            time.sleep(self.game_delay)

            # Prompt for a rematch or to end the game session.
            play_again = input("Press 'R' for a Rematch or any other key to Quit and then press Enter: ").lower()
            if play_again != 'r':
                print("\nThank you for playing Tic-Tac-Toe!\n")
                break

if __name__ == "__main__":
    main()
