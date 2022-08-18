def tic_tac_toe():
    board = ["u1","u2","u3","m1","m2","m3","d1","d2","d3"]
    game_end = False
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def board_draw():
        print(str(board[0]) + "|" + str(board[1]) + "|" + str(board[2]))
        print("--------")
        print(str(board[3]) + "|" + str(board[4]) + "|" + str(board[5]))
        print("--------")
        print(str(board[6]) + "|" + str(board[7]) + "|" + str(board[8]))
        print()

    def player_selection():
        while True:
            try:
                board_n = board.index(input())
                if board_n in range(9):
                    return board_n
                else:
                    print("\nThat option is not valid. Pick one from the board:")
            except ValueError:
                print("\nThat option is not valid. Pick one from the board:")
            continue

    def x_play():
        n = player_selection()
        if board[n] == "X" or board[n] == "O":
            print("\nThat place its already taken. Choose another:")
            x_play()
        else:
            board[n] = "X"

    def o_play():
        n = player_selection()
        if board[n] == "X" or board[n] == "O":
            print("\nThat place its already taken. Choose another:")
            o_play()
        else:
            board[n] = "O"

    def check_result():
        count = 0
        for win in win_comb:
            if board[win[0]] == board[win[1]] == board[win[2]] == "X":
                print("The X Wins!\n")
                return True

            if board[win[0]] == board[win[1]] == board[win[2]] == "O":
                print("The O Wins!\n")
                return True
        for win in range(9):
            if board[win] == "X" or board[win] == "O":
                count += 1
            if count == 9:
                print("We got a Tie\n")
                return True

    while not game_end:
        board_draw()
        game_end = check_result()
        if game_end:
            break
        print("X player insert a place where to put a cross:")
        x_play()
        print()
        board_draw()
        game_end = check_result()
        if game_end:
            break
        print("O Player insert a place where to put a nought:")
        o_play()
        print()

    if input("Do you want to play again? (y/n)\n") == "y":
        print()
        tic_tac_toe()


tic_tac_toe()
