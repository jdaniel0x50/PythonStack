def get_item_type_and_count(item):
    item_type = type(item)
    if item_type.__name__ == 'str':
        length = len(item)
        repeat_char = item[0].lower()
    elif item_type.__name__ == 'int':
        length = item
        repeat_char = '*'
    else:
        return "Error"
    print_repetition(length, repeat_char)

def print_repetition(count_repeat, char_repeat):
    print_string = ""
    for chars in range(count_repeat):
        print_string += char_repeat
    print print_string


# Main Program
# define lists and call functions
my_list = [4, 6, 1, 3, 5, 7, 25]
my_list = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smitth"]

for item in my_list:
    get_item_type_and_count(item)
    