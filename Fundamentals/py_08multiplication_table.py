''' Generates a Multiplication table without taking inputs '''

# define block spacing for the table alignment
# assigns a set container of six digits to a block (cell)
def block_spacing(num):
    spaces = 6 - len(str(num))
    block = ""
    for space in range(spaces):
        block = block + " "
    block = block + str(num)
    return block

# print the header of the multiplication table
# starts the header with x ... the values on top are multipliers
def print_header():
    line = block_spacing("mult x")
    for num in range(1, 13):
        line = line + str(block_spacing(num))
    print line

# print a row in the multiplication table using the multiplier
# the first number in the row is the multiplier
def print_row(multiple):
    line = block_spacing("x " + str(multiple))
    for num in range(1, 13):
        line = line + str(block_spacing(num * multiple))
    print line

print_header()
# set the number of multipliers (rows) in the table
multipliers = 15
for mult in range(1, multipliers+1):
    print_row(mult)