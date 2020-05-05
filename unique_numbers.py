#the program prints out a sorted list of unique elements in a given sample list

def unique(L):
    sample_list2 = list(set(sample_list))
    sample_list2.sort()        
    print("Unique list: ", sample_list2)

sample_list = [1, 2, 3, 4, 2, 2, 3, 4, 55, 6, 4, 3, 3, 7, 6, 8, 5, 7, 5, 44, 2, 333, 67, 8, 6]
unique(sample_list)
