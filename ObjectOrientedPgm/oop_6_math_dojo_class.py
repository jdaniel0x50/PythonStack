class MathDojo(object):
    def __init__(self):
        self.int_value = 0
    def add(self, addend, *addends):
        # gather the collective sum of all arguments through a defined function
        sum_args = sum_all_args(addend, *addends)
        self.int_value += sum_args
        return self
    def subtract(self, subtrahend, *subtrahends):
        # gather the collective sum of all arguments through a defined function
        sum_args = sum_all_args(subtrahend, *subtrahends)
        self.int_value -= sum_args
        return self

def sum_item(my_item):
    # this function is called upon each argument passed to methods add and subtract
    # evaluates the item to determine whether it is a list or tuple
    # if it is a list or tuple, it iterates to generate and return a sum of values
    # if it is not a list or tuple, it returns the value
    my_sum = 0
    if type(my_item) == list or type(my_item) == tuple:
        for items in my_item:
            my_sum += items
    else:
        my_sum = my_item
    return my_sum

def sum_all_args(first_arg, *other_args):
    sum_args = 0
    # evaluate whether first arg was a list or tuple
    sum_args += sum_item(first_arg)
    # if there are extra arguments, iterate through the arguments to create a collected sum
    for arg in other_args:
        arg = sum_item(arg)
        sum_args += arg
    return sum_args


# MAIN PROGRAM
# create new math instance md
md = MathDojo()
# md.add([5, 7, 90], (1,2), [78, 23, 8])
# md.subtract(2.25, [5, 23], 100).add(55, 3000)
md.add([1], 3, 4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3])

# md.add(1, 4, 5, 6, 10)
print md.int_value

