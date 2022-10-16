# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число 
# и показывает сумму его цифр. Через строку нельзя решать.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

userNum = float(input("Введите число: "))
sumDigits = 0
size = len(str(userNum)) - 2
userNum *= 10 ** size

while userNum:
    sumDigits += userNum % 10
    userNum //= 10
    
print(f"Сумма цифр в числе в вашем числе = {int(sumDigits)}")