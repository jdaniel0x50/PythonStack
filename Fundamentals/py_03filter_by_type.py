def check_instance(obj):
    # this defined function checks the passed object's type
    # it then passes the objec to the appropriate length function
    if isinstance(obj, str):
        check_str_length(obj)
    elif isinstance(obj, int):
        check_int_size(obj)
    elif isinstance(obj, list):
        check_list_size(obj)

def check_int_size(my_int):
    # checks the size of an integer object
    if my_int < 100:
        print "That's a small number"
    else:
        print "That's a big number!"

def check_str_length(my_str):
    # checks the size of a string object
    if len(my_str) < 50:
        print "That's a short sentence"
    else:
        print "That's a long ... sentence"

def check_list_size(my_list):
    # checks the size (length) of a list object
    if len(my_list) < 10:
        print "Short list"
    else:
        print "Big list"

# defines the object to be tested for type and length
my_object = [1, 7, 3, 2, 23, 2342, 3, 4234, 234, 234, 2]
# calls the function to test for type and length
check_instance(my_object)
