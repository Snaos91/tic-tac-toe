import snoop

head_line = (" ", "1", "2", "3")
line1 = ["1", "-", "-", "-"]
line2 = ["2", "-", "-", "-"]
line3 = ["3", "-", "-", "-"]
motion_count = 1


def print_playing_field(head_line, line1, line2, line3):  # печать игрового поля
    print(" ".join(head_line))
    print(" ".join(line1))
    print(" ".join(line2))
    print(" ".join(line3))
    return head_line, line1, line2, line3


def input_motion():
    while True:
        try:
            player_line = int(input("Выберите линию 1 или линию 2 или линию 3 для выполнения хода..."))
            player_column = int(input("Выберите столбец 1 или столбец 2 или столбец 3 для выполнения хода... "))
            if 1 <= player_line <= 3 and 1 <= player_column <= 3:
                return [player_line, player_column]
            else:
                raise ValueError
        except ValueError:
            print("Ошибка! Попробуйте снова")


def print_error():
    print("Ход неверный...")


def motion_players1(head_line, line1, line2, line3):  # ход игрока
    list_motion = input_motion()
    if list_motion[0] == 1:
        if line1[list_motion[1]] == "-":
            line1[list_motion[1]] = "x"
        else:
            print_error()
            motion_players1(head_line, line1, line2, line3)
    elif list_motion[0] == 2:
        if line2[list_motion[1]] == "-":
            line2[list_motion[1]] = "x"
        else:
            print_error()
            motion_players1(head_line, line1, line2, line3)
    elif list_motion[0] == 3:
        if line3[list_motion[1]] == "-":
            line3[list_motion[1]] = "x"
        else:
            print_error()
            motion_players1(head_line, line1, line2, line3)
    return head_line, line1, line2, line3


def motion_players2(head_line, line1, line2, line3):  # ход игрока
    list_motion = input_motion()
    if list_motion[0] == 1:
        if line1[list_motion[1]] == "-":
            line1[list_motion[1]] = "o"
        else:
            print_error()
            motion_players2(head_line, line1, line2, line3)
    elif list_motion[0] == 2:
        if line2[list_motion[1]] == "-":
            line2[list_motion[1]] = "o"
        else:
            print_error()
            motion_players2(head_line, line1, line2, line3)
    elif list_motion[0] == 3:
        if line3[list_motion[1]] == "-":
            line3[list_motion[1]] = "o"
        else:
            print_error()
            motion_players2(head_line, line1, line2, line3)
    return head_line, line1, line2, line3


def winner(head_line, line1, line2, line3):
    if line1[1] == line1[2] == line1[3] == "x" or line2[1] == line2[2] == line2[3] == "x" or line3[1] == line3[2] == \
            line3[3] == "x" or line1[1] == line2[1] == line3[1] == "x" or line1[2] == line2[2] == line3[2] == "x" or \
            line1[3] == line2[3] == line3[3] == "x" or line1[1] == line2[2] == line3[3] == "x" or line1[3] == line2[2] \
            == line3[1] == "x":
        print("Выиграл первый игрок!")
    elif line1[1] == line1[2] == line1[3] == "x" or line2[1] == line2[2] == line2[3] == "x" or line3[1] == line3[2] == \
            line3[3] == "x" or line1[1] == line2[1] == line3[1] == "x" or line1[2] == line2[2] == line3[2] == "x" or \
            line1[3] == line2[3] == line3[3] == "x" or line1[1] == line2[2] == line3[3] == "x" or line1[3] == line2[2] \
            == line3[1] == "x":
        print("Выиграл второй игрок!")
    else:
        print("Ничья!")


print_playing_field(head_line, line1, line2, line3)
for motion_count in range(1, 9 + 1):
    if motion_count % 2 != 0:
        print("Ход первого игрока!")
        motion_players1(head_line, line1, line2, line3)
        print_playing_field(head_line, line1, line2, line3)
        motion_count += 1
    else:
        print("Ход второго игрока!")
        motion_players2(head_line, line1, line2, line3)
        print_playing_field(head_line, line1, line2, line3)
        motion_count += 1

winner(head_line, line1, line2, line3)
