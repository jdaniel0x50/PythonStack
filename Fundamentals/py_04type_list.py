def check_instance(obj, my_string, my_sum):
    # this defined function checks the passed object's type
    # it then passes the objec to the appropriate function to concatenate or sum
    if isinstance(obj, str):
        my_string = concatenate_str(obj, my_string)
    elif isinstance(obj, int):
        my_sum = sum_int(obj, my_sum)
    elif isinstance(obj, list):
        print "This function cannot accept a list data type"
    else:
        print "This function cannot accept this data type"
    return [my_string, my_sum]


def concatenate_str(obj, my_string):
    # concatenate the string to the running string
    my_string = my_string + " " + obj
    return my_string

def sum_int(obj, my_sum):
    # add the integer to the running sum
    my_sum = my_sum + obj
    return my_sum


# define my input of type integer or string
# input_list = ['magical unicorns', 19, 'hello', 98, 98, 'world']
# input_list = ['magical unicorns', 'hello', "more text", 'world']
input_list = [1, 23, 35, 74, 865, 234, 2, 2, 9]

# initialize running string and sum
my_string = ""
my_sum = 0

# cycle through the objects in the list
for obj in input_list:
    return_list = check_instance(obj, my_string, my_sum)
    my_string = return_list[0]
    my_sum = return_list[1]

# check the types in the list
if my_string != "" and my_sum != 0:
    input_type = "mixed"
elif my_string == "" and my_sum != 0:
    input_type = "integer"
elif my_string != "" and my_sum == 0:
    input_type = "string"
else:
    input_type = "invalid"  # for case that there were no integers or strings

# print output to user
print "The list was of", input_type, "type"
if input_type == "string" or input_type == "mixed":
    print "The concatenated string =", my_string
if input_type == "integer" or input_type == "mixed":
    print "The running sum =", my_sum
