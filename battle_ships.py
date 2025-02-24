def create_new_map():
    '''
    Создает словарь карты для игры
    :return: словарь карты для игры
    '''
    game_map = {}
    for letter in "АБВГДЕЖЗИК":
        game_map[letter] = [i for i in range(1, 11)]
    return game_map



def choice(game_map, size):
    '''
    :param game_map: словарь игровой
    :param size: длина выставляемого корабля
    :return: логический флаг успешно выставленного корабля
    '''
    while True:
        str_letter, str_number = "", ""
        for i in range(size):
            while True:
                try:
                    letter, number = input("Введите координату- букву\n").upper(), int(input("Введи координтату - число\n"))
                    if letter not in "АБВГДЕЖЗИК" or number not in range(1, 11):
                        print("Неверный ввод координат, попробуй еще")
                        continue
                    elif not check_neighbors_2(letter, number, game_map):
                        print("Несвободное поле")
                        continue
                    else:
                        break
                except ValueError:
                    print("Неверно, братан")              
            str_letter += letter
            str_number += str(number)
        if len(set(str_letter)) == 1 and str_number in "12345678910987654321" or \
                len(set(str_number)) == 1 and str_letter in "АБВГДЕЖЗИКИЗЖЕДГВБА":
            zip_list = zip(list(str_letter), list(str_number))
            for element in zip_list:
                game_map[element[0]][int(element[1]) - 1] = None
            return True
        else:
            print("Неверный размер корабля")
            

def show_game_map(game_map):
    '''
    :param game_map: словарь игровой карты
    :return: функция возвращает None
    '''
    print("* 1 2 3 4 5 6 7 8 9 10")
    for letter in game_map:
        s = letter + " "
        for element in game_map[letter]:
            s += "* " if element else "□ "
        print(s)
    print()


def set_all_ships():
    '''
    Функция выставления всех кораблей
    :return: возращает карту с выставленными вручную кораблями
    '''
    count, full_count = [0, 0, 0, 0], [4, 3, 2, 1]
    game_map = create_new_map()
    while sum(count) < 10:
        number = int(input("Сколькопалубный корабль хочешь поставить ?"))
        if count[number-1] == full_count[number-1]:
            print("Кораблей такого типа поставить больше нельзя!")
        else:
            count[number-1] += 1
            choice(game_map, number)
            show_game_map(game_map)
    return game_map

import random



def check_neighbors_2(letter, number, game_map):

    '''
    :param letter: буквенное значение клетки
    :param number: цифровое значение клетки
    :param game_map: текущий словарь игровой карты
    :return: логическое значение, указыващее можно ли поставить корабль на эту клетку
    '''
    neighbors, letters, indexes = [], [letter], [number]
    string = " АБВГДЕЖЗИК "
    index = string.index(letter)
    symbols_to_check = [string[index-1], string[index+1], number-1, number+1]
    list_copy = symbols_to_check.copy()
    for symbol in list_copy:
        if symbol not in list("АБВГДЕЖЗИК") + list(range(1, 11)):
            symbols_to_check.remove(symbol)
        else:
            if type(symbol) is str:
                letters.append(symbol)
            else:
                indexes.append(symbol)
    for i in letters:
        for j in indexes:
            neighbors.append((i, j))
    neighbors.remove((letter, number))
    for element in neighbors:
        if game_map[element[0]][element[1]-1] is None:
            return False
    return True


def generate_random_ships_2(size, game_map_2):
    '''
    :param size: размер коробля
    :param game_map_2: словарь игровой карты
    :return: логический ключ показывающий можно ли поставить корабль в сгенерированную клетку
    '''
    string = "АБВГДЕЖЗИК"
    list_to_change = []
    type_4 = random.randint(1, 4)
    if type_4 == 1:
        letter = random.choice(list(string))
        number = random.randint(1, 10 - size + 1)
        for i in range(number, number + size):
            if check_neighbors_2(letter, i, game_map_2):
                list_to_change.append((letter, i-1))
            else:
                return False
        for element in list_to_change:
            game_map_2[element[0]][element[1]] = None
        #show_game_map(game_map_2)
        return True
    elif type_4 == 2:
        letter = random.choice(list(string))
        number = random.randint(size, 10)
        for i in range(number-(size-1), number+1):
            if check_neighbors_2(letter, i, game_map_2):
                list_to_change.append((letter, i-1))
            else:
                return False
        for element in list_to_change:
            game_map_2[element[0]][element[1]] = None
        #show_game_map(game_map_2)
        return True
    elif type_4 == 3:
        letter = random.choice(list(string[(size-1):]))
        number = random.randint(1, 10)
        index = string.index(letter)
        for letter in [string[index - i] for i in range(0, size)]:
            if check_neighbors_2(letter, number, game_map_2):
                list_to_change.append((letter, number-1))
            else:
                return False
        for element in list_to_change:
            game_map_2[element[0]][element[1]] = None
        #show_game_map(game_map_2)
        return True
    elif type_4 == 4:
        letter = random.choice(list(string[:-(size-1)])) if size != 1 else random.choice(list(string))
        number = random.randint(1, 10)
        index = string.index(letter)
        for letter in [string[index + i] for i in range(0,size)]:
            if check_neighbors_2(letter, number, game_map_2):
                list_to_change.append((letter, number-1))
            else:
                return False
        for element in list_to_change:
            game_map_2[element[0]][element[1]] = None
        #show_game_map(game_map_2)
        return True
    
    
def generate_all_random_ships():
    '''
    Функция автоматической генерации всех кораблей
    :return: словарь карты со сгенерированными кораблями
    '''
    count_random_ships = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
    game_map_2 = create_new_map()
    while len(count_random_ships) > 0:
        size = random.choice(count_random_ships)
        #print(size)
        if generate_random_ships_2(size, game_map_2):
            count_random_ships.remove(size)
        #print(count_random_ships)
    return game_map_2
#print(map_1, map_2)
import time

def game_process():
    '''
    Функция реализующая последовательный процесс игры
    :return: возврашает None
    '''
    game_mode = int(input("۞ Выбери: 1 - Ты хочешь сам составить карту кораблей, 2 - она сгенерируется автоматически ۞\n"))
    if game_mode == 1:
        map_1 = set_all_ships()
        show_game_map(map_1)
    else: 
        print("۞ Вот твоя карта кораблей: ۞\n")
        map_1 = generate_all_random_ships()
        show_game_map(map_1)      
    map_2 = generate_all_random_ships()
    chiter_list = []
    for letter in map_1.keys():
        for index, element in enumerate(map_1[letter]):
            if element is None:
                chiter_list.append((letter, index+1))
    def show_game_map_in_process(game_map):
        '''
        Функция,отображающая текущее положение кораблей игрока
        :param game_map: текуший словарь игровой карты игрока
        :return: функция возрашает None
        '''
        print("۞ Твоя игровая карта, светлые квадратики - попадания по твоим кораблям ۞\n")
        print("* 1 2 3 4 5 6 7 8 9 10")
        for letter in game_map:
            s = letter + " "
            for element in game_map[letter]:
                if isinstance(element, int):
                    s += "* "
                elif element is None:
                    s += "□ "
                elif element == "0":
                    s += "■ "
                elif element == "1":
                    s += "x "
            print(s)
        print()
    def show_enemy_map_in_process(game_map):
        '''
        Функция, отображабщая текушую информацию по вражеским кораблями
        :param game_map: текущий словарь игровой карты противника
        :return: функция возвращает None
        '''
        print("۞ Карта твоего соперника, квадратики - твои попадания ۞\n")
        print("* 1 2 3 4 5 6 7 8 9 10")
        for letter in game_map:
            s = letter + " "
            for element in game_map[letter]:
                if isinstance(element, str):
                    s += "■ "
                elif isinstance(element, float):
                    s += "x "
                else:
                    s += "◦ "
            print(s)
        print()

    points_1, points_2 = 20, 20
    def play_human(map_2):
        '''
        Функция ввода координта игроком
        :param map_2: текущий словарь игровой карты противника
        :return: функция возвращает None
        '''
        print("۞ Введите координату поля, где по вашему мнению может быть вражеский корабль ۞\n")
        show_enemy_map_in_process(map_2)
        while True:
            try:
                letter, number = input().upper(), int(input())
                if letter == "q":
                    raise BaseException
                if letter not in ("АБВГДЕЖЗИК") or number not in list(range(1, 11)):
                    raise ValueError
                break
            except (ValueError, KeyError):
                print("Неверные координаты, братан, строку там попутал, или число")
        time.sleep(2)
        if map_2[letter][number-1] == None:
            if not check_neighbors_2(letter, number, map_2):
                print("۞ Вы ранили соперника! ۞\n")
                time.sleep(1.5)
                n = random.randint(1, 5)
                if n == 1:
                    print("Ранили, меня ранили!!\n".upper())
                elif n == 2:
                    print("Аййй, болезненно то так, ух ты какой\n".upper())
                elif n == 3:
                    print("Когда ты успел посмотреть в мои карты, они же защищенны шифрованием!\n".upper())
                elif n == 4:
                    print("Какой же ты... Точный одако\n".upper())
                else:
                    print("Я тебе не Титаник, понимаешь ?\n".upper())
            else:
                print("۞ Вы потопили посудину соперника! ۞\n ")
                time.sleep(1.5)
                n = random.randint(1, 5)
                if n == 1:   
                    print("Ты потопил этот жалкий кораблик, для меня это мелочь\n".upper())
                elif n == 2:
                    print("Мелочь, а неприятно, хотя лан, где там твой четырехпалубный стоит ?\n".upper())
                elif n == 3:
                    print("Только и  умеешь, что так банально действовать...\n".upper())
                elif n == 4:
                    print("Опять довольствуешься малым... Лох!\n".upper())
                else:
                    print("Не такая драма как с Ди Каприо, но все же...\n".upper())
            map_2[letter][number-1] = "0"
            time.sleep(1.8) 
            show_enemy_map_in_process(map_2)
            nonlocal points_2
            points_2 -= 1
            if points_2 > 0:
                time.sleep(1)
                play_human(map_2)
        else:
            if points_2 == 0:
                print("бляяяяяя\n".upper())
            else:
                map_2[letter][number-1] = float(number)
                n = random.randint(1, 5)
                if n == 1:
                    print("Ну ты и косоглазый конечно...\n".upper())
                elif n == 2:
                    print("Если бы ты был лучником, то потребовались бы сотни, нет тонны стрел!\n".upper())
                elif n == 3:
                    print("Давай я тебе покажу свои корабли, все равно промажешь ведь...\n".upper())
                elif n == 4:
                    print("Ну это уже скучно, давай ты просто согласишься что лучше я ?\n".upper())
                else:
                    print("И заваривая чай ты мешаешь ложкой воздух ?\n".upper())
                time.sleep(1.7)
                show_enemy_map_in_process(map_2)
            return


    def play_computer(map_1):
        '''
        Функция, реализующая алгоритм хода противника
        :param map_1: текущая словарь игровой карты игрока
        :return: функция возвращает None
        '''
        list_attemps = []
        m = random.choice(list(range(100)))
        if m > 69:
            tuple_1 = random.choice(chiter_list)
            if tuple_1 in list_attemps:
                while True:
                    tuple_1 = random.choice(chiter_list)
                    if tuple_1 not in list_attemps:
                        list_attemps.append(tuple_1)
                        break
            letter, number = tuple_1       
            chiter_list.remove(tuple_1)
        else:
            letter, number = random.choice("АБВГДЕЖЗИК"), random.randint(1, 10)
            if (letter, number) in list_attemps:
                while True:
                    letter, number = random.choice("АБВГДЕЖЗИК"), random.randint(1, 10)
                    if (letter, number) not in list_attemps:
                        list_attemps.append((letter, number))
                        break         
        n = random.randint(1, 5)
        if n == 1:
            print("Итак, мой ход...\n".upper())
        elif n == 2:
            print("Плиииииииииии\n".upper())
        elif n == 3:
            print("Думая твои недокорабли на...\n".upper())
        elif n == 4:
            print("Лови аптечку !\n".upper())
        else:
            print("Ща как плюну, как плюну!!\n".upper())
        time.sleep(random.random()+1)
        print(letter, number, end = "\n\n")
        time.sleep(1.5)
        if map_1[letter][number-1] == None:
            n = random.randint(1, 5)
            if n == 1:
                print("Ахахаха, ну ты и профан!\n".upper())
            elif n == 2:
                print("Баааааааааммммц\n".upper())
            elif n == 3:
                print("Я не ожидал что будет так просто...\n".upper())
            elif n == 4:
                print("Ну куда ты тягаешься с искуственным интеллектом...\n".upper)
            else:
                print("Устанешь швабру выжимать, сдавайся\n".upper())
            nonlocal points_1
            points_1 -= 1
            map_1[letter][number-1] = "0"
            time.sleep(1.5)
            show_game_map_in_process(map_1)
            if points_1 > 0:
                play_computer(map_1)
        else:
            n = random.randint(1, 5)
            if n == 1:
                print("Да как я не попал? В твои недокорабли то ?\n".upper())
            elif n == 2:
                print("Сука, похоже перепил машинного масла, мажу постоянно, уууууух\n".upper())
            elif n == 3:
                print("Да где ты их спрятал то ? Хитрый человек...\n".upper())
            elif n == 4:
                print("Почему можно только по одной клетке стрелять, хочу по всем уже и выиграть наконец...\n".upper())
            else:
                print("Просто  глушу рыбку и дельфинов, я не для этого создан !!")
            map_1[letter][number-1] = "1"
            time.sleep(1.6)
            show_game_map_in_process(map_1)
            return
    while True:
        play_human(map_2)
        time.sleep(1)
        if points_2 == 0:
            print("Вот ты везучий конечно ****** на читах... Как ты победил меня ??\n".upper())
            break
        message_number = random.randint(1, 10)
        if message_number in [9, 10]:
            n = random.randint(1, 3)
            if n == 1:
                time.sleep(1)
                print("\nБлин так скучно с тобой, интереснее на гонки подростковых прыщей смотреть...\n".upper())
            elif n == 2:
                time.sleep(1)
                print("\nCтавки на спорт не желаешь ? Прышки через жирафа там, или скоростное взвещшивание панд ?\n".upper())
            else:
                time.sleep(1)
                string = "\nCкажу по слогам- я устал\n".upper()
                for i in string:
                    time.sleep(0.1)
                    print(i, sep = "", end = "")
                
        play_computer(map_1)
        time.sleep(1)
        if points_1 == 0:
            print("С тобой играть, ахахаах, не смеши меня\n".upper())
            break
        

game_process()
    
    
    



