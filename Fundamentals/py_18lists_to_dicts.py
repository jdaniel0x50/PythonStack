# define lists to create dictionary
name = ['Anna', 'Eli', 'Pariece', 'Brendan', 'Amy', 'Shane', 'Oscar']
favorite_animals = ['horse', 'cat', 'spider', 'giraffe', 'ticks', 'dolphins', 'llamas']

def make_dictionary(list1, list2):
    # the longer list should be used for the key values
    # list identified first in the zip function will define the keys
    if len(list1) > len(list2):
        new_dictionary = dict(zip(list1, list2))
    else:
        new_dictionary = dict(zip(list2, list1))        
    return new_dictionary


# Main Program
new_dictionary = make_dictionary(name, favorite_animals)
print new_dictionary
    