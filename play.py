import os
import time

def clear_screen():
    """Clears the console screen for better visibility."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen based on OS

def draw_board(board):
    """Displays the current state of the game board."""
    # Print the board using formatted strings for clarity
    print(" %c | %c | %c " % (board[1], board[2], board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4], board[5], board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7], board[8], board[9]))
    print("   |   |   ")

def check_position(board, x):
    """Checks if the specified position on the board is empty."""
    return board[x] == ' '  # Returns True if the position is empty

def check_win(board):
    """Checks for a winning condition or a draw."""
    # Define winning combinations
    winning_combinations = [
        (1, 2, 3), (4, 5, 6), (7, 8, 9),  # horizontal
        (1, 4, 7), (2, 5, 8), (3, 6, 9),  # vertical
        (1, 5, 9), (3, 5, 7)  # diagonal
    ]
    # Check each winning combination for a win
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return 1  # Win detected
    # Check if the board is full (draw)
    if all(board[i] != ' ' for i in range(1, 10)):
        return -1  # Draw detected
    return 0  # Game is still running

def play_game():
    """Main function to control the game flow."""
    board = [' '] * 10  # Initialize a list to represent the game board (index 0 unused)
    player = 1  # Start with player 1
    game_state = 0  # Initial game state (running)
    marks = [' ', 'X', 'O']  # Index 1 is X, index 2 is O

    print("Tic-Tac-Toe Game Developed By Mohammed Jawad Ali Shujah")
    print("Player 1 [X] --- Player 2 [O]\n")
    print("Please Wait...")
    time.sleep(1)  # Brief pause for effect

    while game_state == 0:
        clear_screen()  # Clear the screen for better visibility
        draw_board(board)  # Display the current board
        print(f"Player {player}'s turn ({marks[player]})")  # Indicate whose turn it is

        try:
            choice = int(input("Enter the position between [1-9]: "))  # Get player input
            # Validate the chosen position
            if choice < 1 or choice > 9 or not check_position(board, choice):
                print("Invalid position, try again.")
                time.sleep(1)  # Pause before next input
                continue
        except ValueError:
            print("Please enter a valid number.")  # Handle non-integer input
            time.sleep(1)
            continue

        board[choice] = marks[player]  # Update the board with the player's mark
        game_state = check_win(board)  # Check for win or draw
        player = 2 if player == 1 else 1  # Switch player

    clear_screen()  # Clear the screen for the final display
    draw_board(board)  # Display the final board state
    if game_state == -1:
        print("Game Draw")  # Announce a draw
    else:
        print(f"Player {3 - player} Won")  # Announce the winning player

    # Prompt to play again
    if input("Do you want to play again? (y/n): ").lower() == 'y':
        play_game()  # Restart the game

if __name__ == "__main__":
    play_game()  # Start the game when the script is executed
