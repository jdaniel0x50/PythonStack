students_list = [
    {'first_name': 'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

users = {
    'Students': [
        {'first_name': 'Michael', 'last_name': 'Jordan'},
        {'first_name': 'John', 'last_name': 'Rosales'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ],
    'Instructors': [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'Martin', 'last_name': 'Puryear'},
    ]
}

def print_user_category(key_name):
    count = 0
    print "__ " + key_name + " __"
    for user_record in users[key_name]:
        count += 1
        first_name = upper_case(user_record['first_name'])
        last_name = upper_case(user_record['last_name'])
        str_length = get_string_length(first_name, last_name)
        print str(count) + " - " + first_name + " " + last_name + " - " + str(str_length)

def upper_case(string):
    return string.upper()

def get_string_length(string1, string2):
    return len(string1) + len(string2)

# Main Function
## PART I == Print first and last names defined in a dictionary object inside a list
# for student in students_list:
    # iterate through the students in the list
    # print first and last name values based on key in dictionary
    # print student['first_name'] + " " + student['last_name']


## PART II == Print Students and then Instructors from the users dictionary
# include the student number and the number of characters in the name
keys = []
for key in users:
    keys.append(key)
for key in keys:
    print_user_category(key)









# print keys[0]
# for user_record in users[keys[0]]:
#     print user_record['first_name'] + " " + user_record['last_name']
# for instructor in users['Instructors']:
#     print instructor['first_name'] + " " + instructor['last_name']

