# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв"
# my_str = 'Мы неабв очень любим Питон иабв Джавабв'.split()
# print(' '.join([word for word in my_str if 'абв' not in word]))

# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
# Первая часть
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
# if winner == first_player:
#     f.write('Победил first_player')
# else: 
#     f.write('Победил second_player')
# f.close()
# Вторая часть игра с ботом
# import codecs

# f = codecs.open('game.txt','w', "utf-8")
# cnt_player = 2 # количество игроков
# cnt_candies = 2021

# from random import randint

# first_player = randint(1,2) # 1 - бот, 2 - вы
# if first_player == 1:
#     print('Первым ходит бот '  "\n")
#     f.write('Первым ходит бот '  "\n")
# else:
#     print('Первым ходите вы' "\n")
#     f.write('Первым ходите вы' "\n")

# for i in range(1,cnt_candies):
#      f.write(str(i) + ': осталось ')
#      f.write(str(cnt_candies)+' конфет' "\n")
#      print(str(i) + ': осталось '+str(cnt_candies)+' конфет' "\n")
#      if first_player%2!=0:
#        if cnt_candies<=28:
#         print('выйграл бот')
#         f.write('выйграл бот')
#         break
#        else: 
#         step = randint(1,28)
#         print('бот забирает - ' +str(step) +' конфет' "\n")
#         f.write('бот забирает - ' +str(step) +' конфет' "\n")
#         cnt_candies = cnt_candies-step
#      else:
#         if cnt_candies<=28:
#          f.write('вы победитель')
#          print('вы победитель')
#          break
#         else:
#             step = input('сколько конфет вы возьмете? ')
#             f.write('Вы забрали - '+ str(step)+ ' конфет' "\n")
#             print('Вы забрали - '+ str(step)+ ' конфет' "\n")
#             cnt_candies = cnt_candies - int(step)
#      first_player +=1
# f.close()

# Создайте программу для игры в ""Крестики-нолики"".
# from pickle import FALSE


# field = list(range(1,10))

# def draw_field(field):
#     print("-"*13)
#     for i in range(3):
#         print('|',field[0+i*3],'|',field[1+i*3],'|',field[2+i*3],'|')
#         print("-"*13)

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Куда ставим "+player_token+"?")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Некорректный ввод. Вы уверены, что ввели число?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(field[player_answer-1]) not in "XO"):
#                 field[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("Клетка занята")
#         else:
#             print ("Некорректный ввод. Введите число от 1 до 9")

# def check_win(field):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if field[each[0]] == field[each[1]] == field[each[2]]:
#             return field[each[0]]
#     return False

# def main(field):
#     counter = 0
#     win = False
#     while not win:
#         draw_field(field)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(field)
#             if tmp:
#                 print (tmp, "выиграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("Ничья")
#             break
#     draw_field(field)

# main(field)

# draw_field(field)

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
def compress_algorithm(str_input):
    str_output=""
    i=0
    while i < len(str_input):
        cnt = 1
        while i+1<len(str_input) and str_input[i]==str_input[i+1]:
            cnt=cnt+1
            i=i+1
        str_output+=str(cnt)+str_input[i]
        i+=1
    return(str_output)

str_new = 'aaabbbbbcccccddddaaa'
print(compress_algorithm(str_new))
str_old = compress_algorithm(str_new)

def decompress_algoritm(s):
    str_original = ""
    i=0
    while i < len(s):
        cnt = int(s[i])
        for j in range(1,cnt+1):
            str_original+=str(cnt)
        i=i+1
        str_original+=s[i]
        i+=1
    return(str_original)

print (decompress_algoritm(str_old))

