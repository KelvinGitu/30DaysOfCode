#the program calculates the average of numbers whose input is in the form of a string

def average():
    numbers = str(input("Enter a string of numbers: "))
    numbers = numbers.split()

    numbers2 = []
    total = 0
    
    for number in numbers:
        number = int(number)
        total += number
        numbers2.append(number)

    avg = total // len(numbers2)
    print(avg)

average()
