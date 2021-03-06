head_line = (" ", "1", "2", "3")  # Игровое поле
line1 = ["1", "-", "-", "-"]
line2 = ["2", "-", "-", "-"]
line3 = ["3", "-", "-", "-"]
motion_count = 1                  # Счетчик ходов
win = 0                           # Определение победителя


def print_playing_field(head_line, line1, line2, line3):  # печать игрового поля
    print(" ".join(head_line))
    print(" ".join(line1))
    print(" ".join(line2))
    print(" ".join(line3))
    return head_line, line1, line2, line3


def input_motion():                             # Ввод хода, с проверкой на ошибки
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


def print_error():                             # Печать ошибки
    print("Ход неверный...")


def motion_players1(head_line, line1, line2, line3):  # ход игрока 1
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


def motion_players2(head_line, line1, line2, line3):  # ход игрока 2
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


def winner(head_line, line1, line2, line3, win):        # проверка победителя
    if line1[1] == line1[2] == line1[3] == "x" or line2[1] == line2[2] == line2[3] == "x" or line3[1] == line3[2] == \
            line3[3] == "x" or line1[1] == line2[1] == line3[1] == "x" or line1[2] == line2[2] == line3[2] == "x" or \
            line1[3] == line2[3] == line3[3] == "x" or line1[1] == line2[2] == line3[3] == "x" or line1[3] == line2[2] \
            == line3[1] == "x":
        win = 1
        return win
    elif line1[1] == line1[2] == line1[3] == "o" or line2[1] == line2[2] == line2[3] == "o" or line3[1] == line3[2] == \
            line3[3] == "o" or line1[1] == line2[1] == line3[1] == "o" or line1[2] == line2[2] == line3[2] == "o" or \
            line1[3] == line2[3] == line3[3] == "o" or line1[1] == line2[2] == line3[3] == "o" or line1[3] == line2[2] \
            == line3[1] == "o":
        win = 2
        return win
    else:
        win = 0
        return win


print_playing_field(head_line, line1, line2, line3)     # Основная программа
while True:
    for motion_count in range(1, 9 + 1):
        if motion_count % 2 != 0:
            print("Ход первого игрока!")
            motion_players1(head_line, line1, line2, line3)
            print_playing_field(head_line, line1, line2, line3)
            motion_count += 1
        elif motion_count % 2 == 0:
            print("Ход второго игрока!")
            motion_players2(head_line, line1, line2, line3)
            print_playing_field(head_line, line1, line2, line3)
            motion_count += 1
        winner(head_line, line1, line2, line3, win)
        win = winner(head_line, line1, line2, line3, win)
        if motion_count == 9:
            print("Ничья!")
            break
        if win == 1:
            print("Победа первого игрока!")
            break
        elif win == 2:
            print("Победа второго игрока!")
            break
    break
