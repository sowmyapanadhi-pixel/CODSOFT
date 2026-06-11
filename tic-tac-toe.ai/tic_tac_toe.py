# import random
# board = [" " for _ in range(9)]
# def print_board():
#     print()
#     print(f"{board[0]} | {board[1]} | {board[2]}")
#     print("--+---+--")
#     print(f"{board[3]} | {board[4]} | {board[5]}")
#     print("--+---+--")
#     print(f"{board[6]} | {board[7]} | {board[8]}")
#     print()

# def check_winner(player):
#     wins = [
#         [0,1,2],[3,4,5],[6,7,8],
#         [0,3,6],[1,4,7],[2,5,8],
#         [0,4,8],[2,4,6]
#     ]

#     for win in wins:
#         if all(board[i] == player for i in win):
#             return True

#     return False

# current_player = "X"

# while True:
#     print_board()

#     move = int(input(f"Player {current_player}, choose (1-9): ")) - 1

#     if board[move] != " ":
#         print("Position already taken!")
#         continue

#     board[move] ="X"

#     if check_winner("X"):
#         print_board()
#         print(f"🎉 Player {current_player} Wins!")
#         break

#     if " " not in board:
#         print_board()
#         print("🤝 It's a Draw!")
#         break
# # AI Move
#     empty_positions = [i for i in range(9) if board[i] == " "]

#     if empty_positions:
#         ai_move = random.choice(empty_positions)
#         board[ai_move] = "O"
#         print(f"🤖 AI chose position {ai_move + 1}")

#     if check_winner("O"):
#         print_board()
#         print("🤖 AI Wins!")
#         break

#     if " " not in board:
#         print_board()
#         print("🤝 It's a Draw!")
#         break
#     if move < 0 or move > 8:
#         print("Choose a number between 1 and 9")
#         continue

import math

board = [" " for _ in range(9)]

def print_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(player):
    wins = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]

    for win in wins:
        if all(board[i] == player for i in win):
            return True

    return False

def is_draw():
    return " " not in board

def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:
        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(score, best_score)

        return best_score

    else:
        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(score, best_score)

        return best_score

def ai_move():

    best_score = -math.inf
    move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"

while True:

    print_board()

    try:
        move = int(input("Choose position (1-9): ")) - 1

        if move < 0 or move > 8:
            print("Choose a number from 1 to 9")
            continue

        if board[move] != " ":
            print("Position already taken!")
            continue

    except ValueError:
        print("Enter a valid number")
        continue

    board[move] = "X"

    if check_winner("X"):
        print_board()
        print("🎉 You Win!")
        break

    if is_draw():
        print_board()
        print("🤝 Draw!")
        break

    print("🤖 AI is thinking...")
    ai_move()

    if check_winner("O"):
        print_board()
        print("🤖 AI Wins!")
        break

    if is_draw():
        print_board()
        print("🤝 Draw!")
        break