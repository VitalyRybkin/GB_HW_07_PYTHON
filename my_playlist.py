import json

import commands as cmds
import globals as g

g.data = []

help_dict = {
    'h': 'Справка',
    'start': 'Начать работу',
    'Q': 'Завершить работу',
    'add': 'Добавить исполнителя',
    'del': 'Удаление',
    'del -a': 'Удалить всё',
    'del -b': 'Удалить исполнителя',
    'del -s': 'Удалить песню',
    'del -st': 'Удалить стиль',
    'play': 'Воспроизвести',
    'play -a': 'Воспроизвести все',
    'play -b': 'Воспроизвести исполнителя',
    'play -s': 'Воспроизвести песню',
}


print('Добро пожаловать в муз-чат-бот!')
while True:
    cmd = input('Введите комманду (> h - справка, > start - начало работы, > Q - завершить)\n> ')
    if not cmd == 'h' and not cmd == 'start':
        print('Введена неверная команда!')
        continue
    if cmd == 'h':
        cmds.help_output(help_dict)
    if cmd == 'start':
        print('Муз-чат-бот начал свою работу!')
        with open('band_list.json', 'r') as f:
            g.data = json.load(f)
        break
    if cmd == 'Q':
        cmds.quit_mess()

while True:
    cmd = input('Введите комманду (> \'Q\' - завершить): \n> ')
    if cmd not in help_dict:
        print('Команды не существует!')
        continue
    if cmd == 'Q':
        cmds.quit_mess()
    if cmd == 'start':
        print('Муз-чат-бот уже трудится!')
    if cmd == 'h':
        cmds.help_output(help_dict)
    if cmd == 'add':
        cmds.add_singer(g.data)
    if cmd == 'del':
        cmds.del_item(g.data, help_dict)
    if cmd == 'play':
        cmds.play(g.data, help_dict)
        


