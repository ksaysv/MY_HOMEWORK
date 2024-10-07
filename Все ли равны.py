first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
third = int(input("Введите третье целое число: "))

if first == second and first == third:
    print('Если все числа равны между собой', 3)
elif first == second or first == third or second == third:
    print('Если хотя бы 2 из 3 введённых чисел равны между собой', 2)
else:
    print('Если равных чисел среди 3-х вообще нет', 0)