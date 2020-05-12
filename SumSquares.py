def squareSum(n):
    """this function takes in a parameter n and 
    returns the difference between the sum of the 
    squares of the first n natural 
    numbers and the square of the sum."""

    total1 = 0
    total2 = 0
    if num < 0:
        return "Wrong Input"
    elif type(num) == str:
        return "Invalid!"        
    else:
        for number in range(1, num+1):
            num_sqr = number**2
            total1 += num_sqr 
            total2 = total2 + number
            total_sqr = total2**2
        return total_sqr - total1
    
num = int(input("Natural number: "))
print(squareSum(num))
