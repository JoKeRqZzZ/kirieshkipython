import math
number1 = int (input("Введите number1 "))
number2 = int (input("Введите number2 "))
print("действия")
print("1 - сложение двух чисел")
print("2 - вычитание второго числа из первого")
print("3 - умножение двух чисен")
print("4 - деление первого числа на второе ")
print("5 - возведение певрого числа на второе")
print("6 - квадратный корень первого и второго числа")
print("7 - факториал первого и второго числа")
print("8 - синус первого и второго числа")
print("9 - косинус первого и второго числа")
print("10 - тангенс первого и второго числа")
deystviye = input("Введите номер действия ")
if deystviye == "1":
    print(number1+number2)
elif deystviye == "2":
    print(number1-number2)
elif deystviye == "3":
    print(number1*number2)
elif deystviye == "4":
    print(number1/number2)
elif deystviye == "5":
    print(number1**number2)
elif deystviye == "6":
    print(math.sqrt(number1), math.sqrt(number2))
elif deystviye == "7":
    print(math.factorial(number1),math.factorial(number2))
elif deystviye == "8" :
    print(math.sin(number1),math.sin(number2))
elif deystviye == "9":
    print(math.cos(number1),math.cos(number2))
elif deystviye == "10":
    print(math.tan(number1),math.tan(number2))
else:
    print("ошибка")
