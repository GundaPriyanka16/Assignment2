'''Create a function that takes a list of numbers as input and prints the sum of all the numbers in the list.'''

def sum_of_all(list,s): 
    if s == 0 :
        return 0  
    else: 
        return list[s-1] + sum_of_all(list, s-1)

list = [5, 8, 13, 24] 
total = sum_of_all(list, len(list))
print("sum of all : ", total)