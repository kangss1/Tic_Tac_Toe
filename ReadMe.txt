---

# Tic-Tac-Toe Application: Classic Strategy Game

**Version 2.0**

Welcome to Tic-Tac-Toe!

This Python script is a classic implementation of the Tic-Tac-Toe game for two players. Each player takes turns marking their symbol on a 3x3 grid, and the goal is to be the first to get three of their marks in a row horizontally, vertically, or diagonally.

=== HOW TO RUN (User Guide) ===

1. Ensure Python is installed on your system. (https://www.python.org/downloads/)
2. Place the Tic_Tac_Toe.py file in the desired directory.
3. Open a terminal or command prompt.
4. Navigate to the directory containing Tic_Tac_Toe.py.
5. Execute the script by typing 'python3 Tic_Tac_Toe.py' and pressing Enter.

The script will start, and the game board will be displayed in your terminal. Follow the prompts to enter your moves.

=== HOW IT WORKS (Design Logic) ===

1. Program Startup:
When you run Tic_Tac_Toe.py, the main function initiates the game by creating an instance of the TicTacToe class and calling its play_game method.

2. Playing the Game:
The game loop begins, and players input their move by choosing a number from 1 to 9, corresponding to the grid's cell they want to mark.

3. Game Flow Control:
The script dynamically validates user input for correct format and cell availability. If a move is valid, the board is updated. Otherwise, the user is prompted to try again.

4. Deciding the Outcome:
After each move, the script checks for a winner by comparing the current state of the board with predefined winning combinations. The game ends in a tie if no winner is found and all cells are filled.

5. Post-Game Options:
Once a game concludes, the players are given the option to start a new game or exit.

Thank you for playing Tic-Tac-Toe!

# Additional Resources

If you need assistance or want to learn more about Python, you can refer to the official Python documentation or visit educational websites that provide tutorials and examples. 

- Official Python Website: https://www.python.org
- Python Documentation: https://docs.python.org/3/
- W3Schools Python Tutorial: https://www.w3schools.com/python/default.asp

--- 