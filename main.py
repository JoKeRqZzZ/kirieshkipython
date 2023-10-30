import math
try:
    num1 = int(input("Введите number1 : "))
    num2 = int(input("Введите number2 : "))
    print("действия :")
    print("1 - сложение двух чисел")
    print("2 - вычитание второго числа из первого")
    print("3 - умножение двух чисен")
    print("4 - деление первого числа на второе ")
    print("5 - возведение певрого числа на второе")
    print("6 - квадратный корень первого и второго числа")
    print("7 - факториал первого и второго числа")
    print("8 - синус первого числа")
    print("9 - косинус первого  числа")
    print("10 - тангенс первого числа")
    deystviye = input("Введите номер действия ")
    if deystviye == "1":
        print(num1+num2)
    elif deystviye == "2":
        print(num1-num2)
    elif deystviye == "3":
        print(num1*num2)
    elif deystviye == "4":
        if num2 ==0:
            print("деление на 0 нельзя!!!")
        else:
             print(num1/num2)
    elif deystviye == "5":
        print(num1**num2)
    elif deystviye == "6":
        print(math.sqrt(num1), math.sqrt(num2))
    elif deystviye == "7":
        if num1 <= 0 or num2 <= 0:
            print("чел ты")
        else:
            print(math.factorial(num1), math.factorial(num2))
    elif deystviye == "8" :
        num1 = int((input("Напишите количество радианов")))
        radianov=math.radians(num1)
        print(math.sin(radianov))
    elif deystviye == "9":
        num1 = int((input("Напишите количество радианов")))
        radianov=math.radians(num1)
        print(math.cos(radianov))
    elif deystviye == "10":
        num1 = int((input("Напишите количество радианов")))
        radianov=math.radians(num1)
        print(math.tan(radianov))
    else:
        print("ошибка!!!")
except ValueError:
    print("bad")
