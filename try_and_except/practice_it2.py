x = 0
while x == 0:
    try:
        num1 = int(input("Введите число: "))
        num2 = int(input("Введите 2-е число: "))

        x = num1 / num2
        print(x)
    except ZeroDivisionError:
        print("На ноль делить нельзя!")
    except ValueError:
        print("Введите числа!")
    else:
        print("No errors.") 
    finally:
        print("Finally.")