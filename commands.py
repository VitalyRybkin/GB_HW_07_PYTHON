import globals as g
import json
import pygame

text_input = ''
def help_output(help_dict):
    for k, v in help_dict.items():
        print('{0:8s}:{1}'.format(k, v))

def quit_mess():
    print('Муз-чат-бот завершил свою работу!')
    print('До новых встреч в музыкальном эфире!')
    with open('band_list.json', 'w') as f:
        json.dump(g.data, f, indent=2)
    exit()

def quit_input(check_input):
    exit_prove = (check_input == '<')
    if exit_prove:
        still_prove = input('Вы уверены? (">" - да, "<" - нет): ')
        if still_prove == '>':
            return True
    return False

def add_singer(data_list):
    flag = True
    band = ''
    song = ''
    style = ''
    playlist = ''
    file_name = ''

    input_dict = {
        'band': 'Введите исполнителя: ',
        'song': 'Введите название композиции: ',
        'style': 'Введите стиль: ',
        'playlist': 'Введите название плэйлиста: ',
        'file': 'Введите имя файла mp3: '
    }

    new_dict = {
        'band': '',
        'song': '',
        'style': '',
        'playlist': '',
        'file': ''
    }

    print('Добавляем исполнителя (> "<" - прервать ввод):')
    while True:

        for k, v in input_dict.items():
            text_input = input(v)
            if quit_input(text_input):
                flag = False
                break
            else:
                new_dict[k] = text_input

        if not flag:
            for k, v in input_dict.items():
                input_dict[k] = ''
            break

        text_input = input('Добавляем? (> "<" - нет, ">" - да) ')
        if quit_input(text_input):
            break

        data_list.append(new_dict)
        print('Исполнитель успешно добавлен в медиатеку!')
        text_input = input('Мне понравилось! Еще одного добавим? (> "<" - нет, ">" - да) ')
        if text_input == '<':
            break

def del_item(data_list, help_dict):
    flag = True
    print('Начинаем удалять... (> "<" - прервать ввод):')
    temp_cmd = {}
    while True:
        for k, v in help_dict.items():
            idx = v.find('Удал')
            if idx == 0:
                print('{0:10s}:{1}'.format(k, v))
                temp_cmd[k] = v
        cmd_del = input('Введите команду удаления:\n>')

        if cmd_del not in temp_cmd:
            print('Комманды не существует!')
            continue

        if cmd_del == 'del':
            print('Введите подкомманду:')
            continue

        if cmd_del == 'del -a':
            text_input = input('Остановить удаление всех записей из вашего плеера? (> "<" - нет, ">" - да) ')
            if quit_input(text_input):
                flag = False
                break
            else:
                flag = False
                data_list.clear()

        if not flag:
            break

        if cmd_del == 'del -b':
            temp_list = []
            for k, v in enumerate(data_list):
                temp_list.append(v['band'])

            for k,v in enumerate(temp_list):
                print(f'[{k + 1}] - {v}')

            while True:
                text_input = input('Введите номер исполнителя для удаления (> "<" - прервать удаление): ')
                if quit_input(text_input):
                    flag = False
                    break
                else:
                    try:
                        item_to_del = int(text_input)
                    except:
                        print('Введено неверное значение!')
                        continue

                    if int(text_input) - 1 not in range(0, len(temp_list)):
                        print('Введено неверное значение!')
                        continue

                    band = temp_list[int(text_input) - 1]
                    for k, v in enumerate(data_list):
                        if v['band'] == band:
                            text_input = input(f'Точно удаляем {band}? (> "<" - нет, ">" - да) ')
                            if quit_input(text_input):
                                flag = False
                                break
                            else:
                                del data_list[k]
                                break

                    flag = False
                    break

        if not flag:
            break

        if cmd_del == 'del -s':
            temp_list = []
            for k, v in enumerate(data_list):
                temp_list.append(v['song'])

            for k, v in enumerate(temp_list):
                print(f'[{k + 1}] - {v}')

            while True:
                text_input = input('Введите номер песни для удаления (> "<" - прервать удаление): ')
                if quit_input(text_input):
                    flag = False
                    break
                else:
                    try:
                        item_to_del = int(text_input)
                    except:
                        print('Введено неверное значение!')
                        continue

                    if int(text_input) - 1 not in range(1, len(temp_list)):
                        print('Введено неверное значение!')
                        continue

                    song = temp_list[int(text_input) - 1]
                    for k, v in enumerate(data_list):
                        if v['song'] == song:
                            text_input = input(f'Точно удаляем {song}? (> "<" - нет, ">" - да) ')
                            if quit_input(text_input):
                                flag = False
                                break
                            else:
                                del data_list[k]
                                break

                    flag = False
                    break

        if not flag:
            break

        break

def play(data_list, help_dict):
    flag = True
    print('Начинаем воспроизводить... (> "<" - прервать):')
    temp_cmd = {}
    while True:
        for k, v in help_dict.items():
            idx = v.find('Восп')
            if idx == 0:
                print('{0:10s}:{1}'.format(k, v))
                temp_cmd[k] = v

        text_input = input('Введите команду воспроизведения (> "<" - прервать):\n>')
        if quit_input(text_input):
            flag = False
            break

        if not flag:
            break

        cmd_play = text_input

        if cmd_play not in temp_cmd:
            print('Комманды не существует!')
            continue

        if cmd_play == 'play':
            print('Введите подкомманду:')
            continue

        if cmd_play == 'play -s':
            temp_list = []
            for k, v in enumerate(data_list):
                temp_list.append(v['file'])

            while True:
                for k, v in enumerate(temp_list):
                    print(f'[{k + 1}] - {v}')
                text_input = input('Введите композицию (> "<" - прервать): ')
                if quit_input(text_input):
                    flag = False
                    break
                else:
                    try:
                        item_to_play = int(text_input)
                    except:
                        print('Введено неверное значение!')
                        continue

                    if item_to_play - 1 not in range(0, len(temp_list)):
                        print('Введено неверное значение!')
                        continue

                    file = temp_list[int(text_input) - 1]
                    for k, v in enumerate(data_list):
                        if v['file'] == file:
                            pygame.mixer.init()
                            pygame.mixer.music.load('music/' + v['file'])
                            pygame.mixer.music.play()
                            player_cmd = input('-s - стоп: ')
                            if player_cmd == '-s':
                                pygame.mixer.music.stop()
                                flag = False
                                break

        if cmd_play == 'play -b':
            print('Команда в разработке...')


        if cmd_play == 'play -a':
            print('Команда в разработке...')

        if not flag:
            break


