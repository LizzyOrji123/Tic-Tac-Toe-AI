def display_winner(board):
    """Announces the winner or tie."""
    if check_winner(board, "X"):
        print("🎉 You win!")
        return True
    if check_winner(board, "O"):
        print("🤖 AI wins!")
        return True
    if is_tie(board):
        print("It's a tie! 🤝")
        return True
    return False
