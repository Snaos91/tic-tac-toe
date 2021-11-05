game_motion = 1
for game_motion in range(1, 10):
    if game_motion % 2 != 0:
        print("Ход первого игрока...")
        player1_line = int(input())
        player1_column = int(input())
        if 1 == player1_line:
            if line1[player1_column] == "-":
                line1[player1_column] = "x"
            else:
                print("Первый игрок, выбирайте свободное поле! ...")
                player1_line = int(input())
                player1_column = int(input())
        elif player1_line == 2:
            line2[player1_column] = "x"
        elif player1_line == 3:
            line3[player1_column] = "x"
        game_motion += 1
    elif game_motion % 2 == 0:
        print("Ход второго игрока...")
        player2_line = int(input())
        player2_column = int(input())
        if 1 == player2_line:
            line1[player2_column] = "o"
        elif player2_line == 2:
            line2[player2_column] = "o"
        elif player2_line == 3:
            line3[player2_column] = "o"
        game_motion += 1