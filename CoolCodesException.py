def divide(a,b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Division by zero not allowed.")

    except TypeError:
        print("Division possible between numbers only.")
    finally:
        print('Division process ended.')

divide(8,2)
divide(8,0)
divide(8,'abc')