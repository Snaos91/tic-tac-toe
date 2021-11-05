def input_motion():  # ввод хода
    player_line = int(input("Выберите линию 1 или линию 2 или линию 3 для выполнения хода..."))
    player_column = int(input("Выберите столбец 1 или столбец 2 или столбец 3 для выполнения хода... "))
    if 1 <= player_line <= 3 and 1 <= player_column <= 3:
        return [player_line, player_column]
    else:
        print("Ход неверный...")
        input_motion()


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


print(int_motion())
