def primeSum(num):
    """the program returns asum of prime numbers between 1 and an 
    integer taken as the input """                 

    total = 0
    for number in range(1, integer_num + 1):
        if 1 < number < 1000000:
            for n in range(2, number):
                if number % n == 0:
                    break
            else:
                total += number

    print(total)

integer_num = int(input("Integer number: "))
primeSum(integer_num)
