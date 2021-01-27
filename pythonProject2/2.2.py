n = int(input('Введите n:'))
while n > 0 and n < 10:
    n = n**2
    print(n)
    break
else:
    print('Вы ввели неверное число. Диапозон чисел: от 0 до 10')