import random

def generate_random_score():
    # generates and returns a random score between 60 and 100
    random_num = random.randint(60, 100)
    return random_num

def assign_grade(score):
    # receives a numeric score and assigns a letter grade
    if score > 89:
        return "A"
    elif score > 79:
        return "B"
    elif score > 69:
        return "C"
    else:
        return "D"

def print_score(score):
    # receives a numeric score and prints a line with score and letter grade
    # function call to retrieve letter grade happens within this function
    letter_grade = assign_grade(score)
    print "Score: " + str(score) + "; Your Grade is " + letter_grade


# Main Function
# iterate to generate and print scores
num_scores = 10

print "__Scores and Grades__"
for score in range(num_scores):
    print_score(generate_random_score())
print "__End of the program. Bye!!__"