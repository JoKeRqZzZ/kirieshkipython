import math
try:
    number1 = int(input("Введите number1: "))
    number2 = int(input("Введите number2: "))

    print("действия")
    print("1 - сложение двух чисел")
    print("2 - вычитание второго числа из первого")
    print("3 - умножение двух чисел")
    print("4 - деление первого числа на второе")
    print("5 - возведение первого числа в степень второго")
    print("6 - квадратный корень первого и второго числа")
    print("7 - факториал первого и второго числа")
    print("8 - синус первого числа")
    print("9 - косинус первого числа")
    print("10 - тангенс первого числа")

    deystviye = input("Введите номер действия: ")


    deystviye = input("Введите номер действия: ")

    if deystviye == "1":
        print(number1 + number2)
    elif deystviye == "2":
        print(number1 - number2)
    elif deystviye == "3":
        print(number1 * number2)
    elif deystviye == "4":
        if number2 == 0:
            print("деление на 0 нельзя")
        else:
            print(number1 / number2)
    elif deystviye == "5":
        print(number1 ** number2)
    elif deystviye == "6":
        print(math.sqrt(number1), math.sqrt(number2))
    elif deystviye == "7":
        print(math.factorial(number1), math.factorial(number2))
    elif deystviye == "8":
        number1 = int(input("Напишите количество радианов: "))
        radianov = math.radians(number1)
        print(math.sin(radianov))
    elif deystviye == "9":
        number1 = int(input("Напишите количество радианов: "))
        radianov = math.radians(number1)
        print(math.cos(radianov))
    elif deystviye == "10":
        number1 = int(input("Напишите количество радианов: "))
        radianov = math.radians(number1)
        print(math.tan(radianov))
    else:
        print("ошибка")
except ValueError:
    print("Ошибка ввода числа")
