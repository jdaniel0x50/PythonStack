'''
Multiples, Sum, and Average Assignment
'''
# MULTIPLES LISTS
# Part I: Print all odd numbers from 1 to 1000
def print_all_odd(max_range):
    for i in range(1, max_range, 2):
        print i

# Part II: Create a program that prints all multiples of 5 from 5 to 1,000,000
def print_multiples_5(max_range):
    for i in range(5, max_range, 5):
        print i


# SUM LIST: Create a program that prints the sum of all values in the list a = [1, 2, 5, 10, 255, 3]
def print_sum_list(list):
    sum_list = 0
    for val in list:
        sum_list += val
    return sum_list

# AVERAGE LIST: Create a program that prints the average of the values in the list
def print_average_list(list):
    sum_list = print_sum_list(list)
    avg_list = sum_list / len(list)
    return avg_list

# print_all_odd(max_range = 1000)
# print_multiples_5(max_range = 1000000)
alist = [1, 2, 5, 10, 255, 3]
print "The sum of the list is", print_sum_list(alist)

blist = [1, 2, 5, 10, 255, 3]
print "The average of the list is", print_average_list(blist)