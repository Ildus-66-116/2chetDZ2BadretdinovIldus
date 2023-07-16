# Задача 10: 

# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

from random import randint

monet = int(input('Введите количество монет: '))
temp = 0
count_resh = 0
count_orel = 0
for _ in range(monet):
    temp = randint(0, 1)
    print(temp, end=' ')
    if temp > 0:
        count_resh += 1
    else:
        count_orel += 1
print()
if count_resh > count_orel:
    print(f'Переверните орлы - {count_orel} раз')
else:
    print(f'Переверните решки - {count_resh} раз')
