# 1. в файле находится N натуральных чисел, записанных через пробел, в последовательности не хватает одного, чтобы 
# выполнялось условие, что каждое следующее на 1 больше предыдущего, найти это число
# num = [1, 2, 3, 5]
# def fun(num):
#     for i in range(0,len(num)):
#         if (num[i+1]-num[i]!=1):
#             return num[i]+1

# with open ('numfile.txt','r') as data:
#     num = data.read()
# num = list(map(int,num.split()))

# print(fun(num))

# Решенеи преподавателя
# my_list = [1, 2, 4, 5]
# res = [(my_list[i]-1) for i in range(1,len(my_list)) if (my_list[i]-1)!=my_list[i-1]]
# print(res)

# 2. Дан список чисел. Создайте список в который попадают числа, описываемые возрастающую последовательность
# num = [1,5,2,3,4,6,1,7]
# def nextmax(listt):
#     max=listt[0]
#     res=[listt[0]]
#     for i in range(len(listt)):
#         if listt[i]>max:
#             max=listt[i]
#             res.append(max)
#     return res
# print(nextmax(num))

# Решение преподавателя
# my_list = [1,5,2,3,4,6,1,7]
# res = [my_list[0]]
# [res.append(item) for item in my_list if item>res[-1]]
# print(res)

# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв"
# print(' '.join(filter(lambda x: not 'абв' in x, 'Мы неабв очень любим Питон иабв Джавабв'.split())))
# Решение преподавателя
my_str = 'Мы неабв очень любим Питон иабв Джавабв'.split()
print(' '.join([word for word in my_str if 'абв' not in word]))
