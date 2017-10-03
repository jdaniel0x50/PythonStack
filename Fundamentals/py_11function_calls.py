def count_odd_even(max_num):
    # iterates through a range of numbers to the maximum number
    # deterimines whether odd or even and prints
    for num in range(max_num + 1):
        odd_even = check_odd_even(num)
        print "Number is " + str(num) + ". This is an " + odd_even + " number."

def check_odd_even(num):
    # function used to determine whether odd or even
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

def multiply_by_multiplier(list, mult):
    # receives list and multiplies each item by the multiplier
    for i in range(len(list)):
        list[i] *= mult
    return list

def layered_multiples(list):
    # receives list of numbers and returns a nested array with 1s to represent the value
    print "The list to iterate is " + str(list) + ". -- The output should have the corresponding number of 1s in nested lists."
    for i in range(len(list)):
        temp_val = list[i]
        list[i] = []
        for j in range(temp_val):
            list[i].append(1)
    return list


max_num = 2000
# my_list = [2, 4, 6, 8, 10, 16, 25, 36, 45, 52]
my_list = [2, 4, 6, 8]
multiplier = 2

# count_odd_even(max_num)
print multiply_by_multiplier(my_list, multiplier)
print layered_multiples(multiply_by_multiplier(my_list, multiplier))