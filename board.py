def create_board():
    """Creates an empty game board."""
    return [" " for _ in range(9)]

def print_board(board):
    """Displays the Tic-Tac-Toe board."""
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i+1]} | {board[i+2]}")
        if i < 6:
            print("-" * 9)
