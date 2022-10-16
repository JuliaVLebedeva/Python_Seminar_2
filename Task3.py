# Задача 3. Напишите программу, в которой пользователь 
# будет задавать две строки, а программа - определять количество 
# вхождений одной строки в другой. COUNT или FIND нельзя юзать! говорил же на семинаре.

string1 = input("Введите строку1: ")
string2 = input("Введите строку2: ")
count = 0
for i in range(len(string1) - len(string2) + 1):
     if string1[i : i + len(string2)] == string2:
         count += 1
print(f'Всего вхождений {string2} в строке {string1} = {count}')