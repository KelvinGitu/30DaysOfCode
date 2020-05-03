def even_odd(list_of_num):
    even_num = list(filter(lambda number: number % 2 == 0, numbers))
    print("Number of even numbers: ", len(even_num))

    odd_num = list(filter(lambda number: number % 2 != 0, numbers))
    print("Number of odd numbers: ", len(odd_num))

numbers = range(51, 112)
even_odd(numbers)