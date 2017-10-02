def list_compare(list_one, list_two):
    if list_one == list_two:
        return True
    else:
        return False

#deine inputs
# list_one = [1, 2, 5, 6, 2]
# list_two = [1, 2, 5, 2, 6]
list_one = ['celery', 'carrots', 'bread', 'milk']
list_two = ['celery', 'carrots', 'bread', 'milk']

#execute list compare
print(list_compare(list_one, list_two))