first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second == third:
    print('Вывод: 3')
elif first == second or first == third or second == third:
    print('Вывод: 2')
else:
    print('Вывод: 0')                                       #Делая эту домашку не внимательно прочитал условия
                                                            # не внимательно прочитал что нужно ввести те цифры в консоль
                                                            #То есть через команду input