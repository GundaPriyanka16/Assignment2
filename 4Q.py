'''
Write a Python function to find the maximum number in a list of numbers.''' 

def max_number(list): 
    max = list[0] 
    for i in list: 
        if i > max: 
            max = i 

    return max

list = [10, 6, 26, 74]  
print("Maximum number: ", max_number(list))
