''' 
This program will evaluate each number between 100 and a maximum
to determine whether the number is prime or a perfect square
'''

def check_prime_square(num):
    # only need to check up to half the possible divisors
    # anything over half would be repeating a check already completed
    half_num = int(num / 2)
    # initialize by assuming the number is prime (has no divisors)
    is_prime = True
    # initialize by assuming the number is not a perfect square
    is_perfect_square = False
    square_poss = check_perfect_square_possible(num)

    for divisor in range(2, half_num+1):
        # only run this check if the number is currently prime
        if is_prime == True:
            # if there is a divisor (no modulo / remainder) then the number is not prime
            if num % divisor == 0:
                is_prime = False
        # only run this check if the number is not a perfect square yet
        # and if the number can possibly be a perfect square (from functional check above)
        if square_poss == True:
            if is_perfect_square == False:
                # if a divisor can multiply by itself to equal the number,
                # the number is a perfect square
                if divisor * divisor == num:
                    is_perfect_square = True
    return [is_prime, is_perfect_square]

def check_perfect_square_possible(num):
    square_poss = False
    last_digit = num % 10
    # FIRST TEST - A number can be a perfect square ONLY if the last digits are 1, 4, 5, 6, 9, or 00
    if num % 100 == 0:
        # check if the last digits are 00
        square_poss = True
    elif last_digit == 1 or last_digit == 4 or last_digit == 5 or last_digit == 6 or last_digit == 9:
        # otherwise check if the last digit is another possible digit
        square_poss = True
    else:
        # a square is not possible for digits ending in 2, 3, 7, or 8
        return False
    
    # SECOND TEST - if the last digits test clear, then the single-digit sum of all the number's digits must add to equal 1, 4, 7, or 9
    digit_sum = sum_digits(num)
    while len(str(digit_sum)) > 1:
        digit_sum = sum_digits(digit_sum)
    if digit_sum == 1 or digit_sum == 4 or digit_sum == 7 or digit_sum == 9:
        return True
    else:
        return False

def sum_digits(num):
    digit_sum = 0
    while num:
        digit_sum += num % 10
        num //= 10
    return digit_sum

# initialize the start and stop values for this prime and square check
start = 100
end = 50000
# initialize print values
str_prime = "Foo! ... %s is a prime number"
str_square = "Bar! ... %s is a perfect square"
str_neither = "FooBar // %s"
count_prime = 0
count_square = 0

for num in range(start, end + 1):
    return_flag = check_prime_square(num)
    # return[0] is the prime flag; True = prime
    # return[1] is the perfect square flag; True = perfect square
    if return_flag[0]:
        # num is prime
        print str_prime % str(num)
        count_prime += 1
    elif return_flag[1]:
        # num is a perfect square (by definition this is not prime)
        print str_square % str(num)
        count_square += 1
    else:
        # neither prime nor perfect square
        print str_neither % str(num)

# print the total number of prime numbers and perfect squares
print "*** There were {} prime numbers, and {} perfect square numbers in the range ***".format(count_prime, count_square)