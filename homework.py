# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв"
# my_str = 'Мы неабв очень любим Питон иабв Джавабв'.split()
# print(' '.join([word for word in my_str if 'абв' not in word]))

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# import codecs
# f = codecs.open('game.txt','w', "utf-8")
# cnt_player = 2 # количество игроков
# cnt_candies = 2021
# from random import randint
# first_player = randint(1,2)
# if first_player ==1:
#     second_player = 2
#     f.write('Первым ходит first_player'  "\n")
#     f.write('Вторым ходит second_player' "\n")
# else:
#     second_player =1
#     f.write('Первым ходит second_player' "\n")
#     f.write('Вторым ходит first_player' "\n")

# for i in range(1,cnt_candies):
#     f.write(str(i) + ' раунд: осталось ')
#     f.write(str(cnt_candies)+' конфет' "\n")
#     if cnt_candies<=28:
#         winner = 1
#         break
#     else:
#         step1 = randint(1,28)
#         f.write('первый забирает - ' +str(step1) +' конфет' "\n")
#         cnt_candies = cnt_candies-step1
#     if cnt_candies<=28:
#         winner = 2
#         break
#     else: 
#         step2 = randint(1,28)
#         f.write('второй забирает - '+ str(step2)+ ' конфет' "\n")
#         cnt_candies = cnt_candies-step2
# print(winner)
# if winner == first_player:
#     f.write('Победил first_player')
# else: 
#     f.write('Победил second_player')
# f.close()

