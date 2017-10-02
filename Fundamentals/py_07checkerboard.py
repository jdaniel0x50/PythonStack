red_square = "*"
white_square = " "

def print_line_1():
    line = ""
    for squares in range(8):
        if squares % 2 == 0:
            line += red_square
        else:
            line += white_square
    return line

def print_line_2():
    line = ""
    for squares in range(8):
        if squares % 2 == 0:
            line += white_square
        else:
            line += red_square
    return line

for lines in range(8):
    if lines % 2 == 0:
        print(print_line_1())
    else:
        print(print_line_2())
