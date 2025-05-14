from board import create_board, print_board
from player import get_user_move
from ai import get_ai_move
from utils import display_winner

def main():
    """Main game loop where user and AI take turns."""
    print("Welcome to Tic-Tac-Toe!")
    board = create_board()
    print_board(board)

    for turn in range(9):  # Max 9 turns in a game
        if turn % 2 == 0:  # User's turn
            move = get_user_move(board)
            board[move] = "X"
        else:  # AI's turn
            move = get_ai_move(board)
            board[move] = "O"
            print(f"AI chooses position {move + 1}")

        print_board(board)

        if display_winner(board):
            return

if __name__ == "__main__":
    main()
