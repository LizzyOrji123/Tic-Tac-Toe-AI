def get_user_move(board):
    """Gets a valid move from the user."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                return move
            print("Invalid move, try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")
