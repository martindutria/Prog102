def tic_tac_toe():
    game_board = [" "," "," "," "," "," "," "," "," "]
    board = ["u1","u2","u3","m1","m2","m3","d1","d2","d3"]
    game_end = False
    win_comb = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def board_draw():
        print(" Places     Game board")
        print(board[0] + "|" + board[1] + "|" + board[2]+"       "+game_board[0] + "|" + game_board[1] + "|" + game_board[2])
        print("--------       -----")
        print(board[3] + "|" + board[4] + "|" + board[5]+"       "+game_board[3] + "|" + game_board[4] + "|" + game_board[5])
        print("--------       -----")
        print(board[6] + "|" + board[7] + "|" + board[8]+"       "+game_board[6] + "|" + game_board[7] + "|" + game_board[8])
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
        if game_board[n] == "X" or game_board[n] == "O":
            print("\nThat place its already taken. Choose another:")
            x_play()
        else:
            game_board[n] = "X"

    def o_play():
        n = player_selection()
        if game_board[n] == "X" or game_board[n] == "O":
            print("\nThat place its already taken. Choose another:")
            o_play()
        else:
            game_board[n] = "O"

    def check_result():
        count = 0
        for win in win_comb:
            if game_board[win[0]] == game_board[win[1]] == game_board[win[2]] == "X":
                print("The X Wins!\n")
                return True

            if game_board[win[0]] == game_board[win[1]] == game_board[win[2]] == "O":
                print("The O Wins!\n")
                return True
        for win in range(9):
            if game_board[win] == "X" or game_board[win] == "O":
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
