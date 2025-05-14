def check_winner(board, player):
    """Checks if the given player ('X' or 'O') has won."""
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]  # Diagonals
    ]
    return any(all(board[pos] == player for pos in condition) for condition in win_conditions)

def is_tie(board):
    """Checks if the game is a tie."""
    return " " not in board
