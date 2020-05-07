def averageMultiple(number):
    """ takes in a number and returns the average multiples 
    of 3 and 5 between 1 and num(num not inclusive)
    """
    
    total = 0
    total_num = 0
    if 1 < num <5000:
        for i in range(1, num):
            if i % 5 == 0 or i % 3 == 0:
                total += i
                total_num += 1
        average = total / total_num
        return average

num = int(input("Number: "))
print(averageMultiple(num))
