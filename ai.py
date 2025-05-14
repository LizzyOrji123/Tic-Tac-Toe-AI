import random
from rules import check_winner

def get_ai_move(board):
    """AI selects an available spot strategically."""
    available_moves = [i for i in range(9) if board[i] == " "]

    # AI strategy: Try to win or block the user
    for move in available_moves:
        board[move] = "O"
        if check_winner(board, "O"):
            return move
        board[move] = "X"
        if check_winner(board, "X"):
            return move
        board[move] = " "  # Reset after testing

    # If no immediate win or block, pick randomly
    return random.choice(available_moves)
