def fibonacciIt(num):
    """this function returns True if a number is in 
    the fibonacci sequence and False if otherwise"""
    a=1
    b=2

    n = 10000
    list_sequence = [1, 2]
    for i in range(0, n+1):
        b=a+b
        a=b-a
        list_sequence.append(b)
    if num < 0:
        return "Wrong input"
    elif type(num) != int:
        return"Invalid"
    elif num in list_sequence:
        return True
    else:
        return False

number = int(input('Integer: '))
fibonacciIt(number)
