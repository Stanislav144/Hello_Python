# ПОБЕДИТЕЛИ СОРЕВНОВАНИЙ

# count = int(input('How many participants?: '))
# i = count
# list = []
# while i > 0:
#     participant = input(f'Who took the {i} place?: ')
#     list.append(participant)
#     i -= 1
# print('The competitions involved: ', sorted(list))
# list.reverse()
# result = list[:3]
# print(f'Winners: {result} Congratulations!')


# 1: Даны два произвольные списка. Удалите из первого списка элементы присутствующие во втором списке.
# #     Примечание. Списки создайте вручную, например так:

# # Решение 1 (со множествами)
# my_list_1 = [2, 5, 8, 2, 12, 12, 4]
# my_list_2 = [2, 7, 12, 3]

# my_set_1 = set(my_list_1)
# # print(type(my_set_1))
# my_set_2 = set(my_list_2)
# # print(type(my_set_2))

# intersection_set = my_set_1 & my_set_2
# # print(intersection_set)
# intersection_list = list(intersection_set)
# for i in intersection_list:
#     my_list_1.remove(i)
# print(my_list_1)

# # Решение 2 (со строками)
my_list_1 = [1, 1, 1, 2, 2, 2, 3, 4]
my_list_2 = [2, 4, 5]
for i in my_list_2:
    while i in my_list_1:
        my_list_1.remove(i)
print(my_list_1)


# 2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

# day_date_dict = {
#     '01': 'первое',
#     '02': 'второе',
#     '03': 'третье',
#     '04': 'четвертое',
#     '05': 'пятое',
#     '06': 'шестое',
#     '07': 'седьмое',
#     '08': 'восьмое',
#     '09': 'девятое',
#     '10': 'десятое',
#     '11': 'одинадцатое',
#     '12': 'двенадцатое',
#     '13': 'тринадцатое',
#     '14': 'четырнадцатое',
#     '15': 'пятнадцатое',
#     '16': 'шестнадцатое',
#     '17': 'семнадцатое',
#     '18': 'восемнадцатое',
#     '19': 'девятнадцатое',
#     '20': 'дватцатое',
#     '21': 'двадцать первое',
#     '22': 'двадцать второе',
#     '23': 'двадцать третье',
#     '24': 'двадцать четвертое',
#     '25': 'двадцать пятое',
#     '26': 'двадцать шестое',
#     '27': 'двадцать седьмое',
#     '28': 'двадцать восьмое',
#     '29': 'двадцать девятое',
#     '30': 'тридцатое',
#     '31': 'тридцать первое'
# }

# month_date_dict = {
#     '01': 'января',
#     '02': 'февраля',
#     '03': 'марта',
#     '04': 'апреля',
#     '05': 'мая',
#     '06': 'июня',
#     '07': 'июля',
#     '08': 'августа',
#     '09': 'сентября',
#     '10': 'октября',
#     '11': 'ноября',
#     '12': 'декабря'
# }

# user_date = input("Введите дату в формате dd.mm.yyyy: ")
# dd, mm, yyyy = user_date.split('.')
# print(f'{day_date_dict[dd]} {month_date_dict[mm]} {yyyy} года')

# 3: Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
#     Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
# В этом случае ответ будет:
# [5, 8]

# my_list_1 = [12, 2, 2, 2, 5, 12, 8, 2, 12]
# for i in my_list_1:
#     while i in my_list_1:
#         my_list_1.remove(i)
# print(my_list_1)