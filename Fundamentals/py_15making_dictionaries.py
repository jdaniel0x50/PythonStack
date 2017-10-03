# Define Dictionary
my_dictionary = {
    'name' : 'Josh',
    'age' : 37,
    'country_of_birth' : 'United States',
    'places_I_have_lived' : ['Michigan', 'Ohio', 'Massachussettes', 'India', 'California', 'Tennessee', 'Illinois']
}

def print_dict_key_value(key, value):
    # evaluate the type of the value parameter
    # construct a string with the key and value, dependent on type
    key = key_no_line(key)
    item_type = get_item_type(value)
    if item_type == 'int':
        is_are = 'is'
        value = str(value)
    elif item_type == 'list':
        if len(value) > 1:
            is_are = 'are'
        else:
            is_are = 'is'
        temp_list = value
        value = ""
        for list_item in temp_list:
            value += str(list_item) + ', '
        value = value[:len(value)-2]
    else:
        is_are = 'is'
    print "My " + key + " " + is_are + " " + value


def get_item_type(item):
    # return the item type (e.g., 'str' or 'int')
    return type(item).__name__

def key_no_line(key):
    # return the key name without any underscores
    # replace with spaces
    return key.replace("_", " ")

# Main Function
for key, value in my_dictionary.iteritems():
    print_dict_key_value(key, value)
