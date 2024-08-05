import random
import time


def show(pos_dict):
    print(        '\n ' + pos_dict[1], pos_dict[2], pos_dict[3] + '\n',
                          pos_dict[4], pos_dict[5], pos_dict[6] + '\n',
                          pos_dict[7], pos_dict[8], pos_dict[9])


def victory(list_vpositions, pos_dict, counter, show_result=False):
    if counter == 10 and show_result:
        print('Ничья')
        return True
    for i in ['[X]', '[0]']:
        for n1, n2, n3 in list_vpositions:
            if pos_dict[n1] == i and pos_dict[n2] == i and pos_dict[n3] == i:
                if show_result:
                    print('Победа', i)
                return True


def input_position(i):
    while True:
        try:
            select_position = int(input('Select position for ' + str(i) + ': '))
            if 1 <= select_position <= 9:
                break
            else:
                print('Please enter 1 - 9')
        except ValueError:
            print('Please enter number')
    return select_position


def input_mode():
    """
    Метод для ввода только цифр от 1 до 9
    :return:
    """
    while True:
        try:
            game_mode = int(input('Select game mode for: '))
            if 1 <= game_mode <= 3:
                break
            else:
                print('Please enter 1 - 3')
        except ValueError:
            print('Please enter number')
    return game_mode


def pc_logik(list_vpositions, pos_dict):
    """
        Логика компьютера основана на случайном выборе свободной ячейки
    :param list_vpositions: выигрышные комбинации для анализа
    :param pos_dict: матрица для определения свободных значений
    :return: номер случайной свободной ячейки
    """
    algoritm_position = 0
    list_analize = []
    for i in pos_dict:
        if pos_dict[i] == '[0]':
            list_analize.append(True) # Компьютер - должен выиграть
        elif pos_dict[i] == '[X]':
            list_analize.append(False) # Игрок - должен проиграть
        elif pos_dict[i] == '[ ]':
            list_analize.append('Zero')

    print('list_vpositions', list_vpositions)
    print('list_analize', list_analize)
    print('pos_dict', pos_dict)
    for n1, n2, n3 in list_vpositions:
        print(list_analize[n1 - 1], list_analize[n2 - 1], list_analize[n3 - 1])
        #### Начало секции для выигрыша - заполнить третья ячейку
        if list_analize[n1 - 1] == True and list_analize[n2 - 1] == True and list_analize[n3 - 1] == 'Zero':
            print('Нужно ставить на', n3)
            return n3
        elif list_analize[n1 - 1] == True and list_analize[n2 - 1] == 'Zero' and list_analize[n3 - 1] == True:
            print('Нужно ставить на', n2)
            return n2
        elif list_analize[n1 - 1] == 'Zero' and list_analize[n2 - 1] == True and list_analize[n3 - 1] == True:
            print('Нужно ставить на', n1)
            return n1
        #### Конец секции для выигрыша

        #### Начало секции для защиты - не дать поставить 3 подряд
        #### Конец секции для защиты

        # print(n1 - 1, n2 - 1, n3 - 1)
        # if n1 and n2 and n3:


    list_free = []
    for i in pos_dict:
        if pos_dict[i] == '[ ]':
            list_free.append(i)
    if len(list_free) > 0:
        rand_int = random.randint(0, len(list_free) - 1)

    elif len(list_free) - 1 == 0:
        rand_int = 0

    print(list_free, rand_int)
    time.sleep(1)
    select_position = list_free[rand_int]
    print('Ставит на позицию:', select_position)
    # print('А можно было поставить на позицию:', algoritm_position)
    return select_position


if __name__ == "__main__":

    list_vpositions = [[1, 2, 3], [1, 4, 7], [1, 5, 9],
                       [4, 5, 6], [2, 5, 8], [3, 5, 7],
                       [7, 8, 9], [3, 6, 9]]

    print('Select game mode:\n'
          '1. User vs User\n'
          '2. User vs PC\n'
          '3. PC vs PC')

    mode = input_mode()
    counter = 0

    pos_dict = {}
    for i in range(1, 10):
        pos_dict[i] = '[ ]'
    show(pos_dict)

    while not victory(list_vpositions, pos_dict, counter, True):
        for i in ['[X]', '[0]']:
            counter += 1
            if victory(list_vpositions, pos_dict, counter):
                continue
            position = ''
            if mode == 1:
                position = input_position(i)
            elif mode == 2:
                if i == '[0]':
                    position = pc_logik(list_vpositions, pos_dict)
                else:
                    position = input_position(i)
            elif mode == 3:
                position = pc_logik(list_vpositions, pos_dict)
            if pos_dict[position] == '[ ]':
                pos_dict[position] = i
            else:
                while True:
                    if pos_dict[position] == '[X]' or pos_dict[position] == '[0]':
                        show(pos_dict)
                        position = ''
                        if mode == 1:
                            position = input_position(i)
                        elif mode == 2:
                            if i == '[0]':
                                position = pc_logik(list_vpositions, pos_dict)
                            else:
                                position = input_position(i)
                        elif mode == 3:
                            position = pc_logik(list_vpositions, pos_dict)

                    else:
                        pos_dict[position] = i
                        break
            show(pos_dict)
