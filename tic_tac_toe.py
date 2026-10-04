board = [" " for _ in range(9)]


def display_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()


def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if all(board[i] == player for i in combination):
            return True

    return False


def computer_move():
    # Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                return
            board[i] = " "

    # Block player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                return
            board[i] = " "

    # Choose first available position
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return


print("Welcome to Tic-Tac-Toe!")
print("You are X and computer is O.")
print("Choose positions from 1 to 9.")

while True:
    display_board()

    try:
        position = int(input("Enter your position (1-9): ")) - 1

        if position < 0 or position > 8:
            print("Please enter a number from 1 to 9.")
            continue

        if board[position] != " ":
            print("That position is already occupied.")
            continue

        board[position] = "X"

    except ValueError:
        print("Please enter a valid number.")
        continue

    if check_winner("X"):
        display_board()
        print("Congratulations! You win!")
        break

    if " " not in board:
        display_board()
        print("It's a draw!")
        break

    computer_move()

    if check_winner("O"):
        display_board()
        print("Computer wins!")
        break

    if " " not in board:
        display_board()
        print("It's a draw!")
        break