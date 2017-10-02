def check_instance(obj):
    if isinstance(obj, str):
        check_str_length(obj)
    elif isinstance(obj, int):
        check_int_size(obj)
    elif isinstance(obj, list):
        check_list_size(obj)

def check_int_size(my_int):
    if my_int < 100:
        print "That's a small number"
    else:
        print "That's a big number!"

def check_str_length(my_str):
    if len(my_str) < 50:
        print "That's a short sentence"
    else:
        print "That's a long ... sentence"

def check_list_size(my_list):
    if len(my_list) < 10:
        print "Short list"
    else:
        print "Big list"

my_object = [1, 7, 3, 2, 23, 2342, 3, 4234, 234, 234, 2]
check_instance(my_object)
