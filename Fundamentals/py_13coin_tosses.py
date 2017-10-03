import random

def generate_random_toss():
    # generates and returns a random coin toss (heads or tails; 0 or 1)
    random_num = random.randint(0, 1)
    if random_num == 0:
        return "head"
    elif random_num == 1:
        return "tail"

def print_line(dict_coin_tosses):
    # print individual lines to tell the user result of coin tosses
    # increments total count of heads and tails
    rand_toss = generate_random_toss()
    dict_coin_tosses['toss_number'] += 1
    if rand_toss == "head":
        dict_coin_tosses['tot_heads'] += 1
    else:
        dict_coin_tosses['tot_tails'] += 1
    print ("Attempt #" + str(dict_coin_tosses['toss_number']) + ": "
           "Throwing a coin ... It's a " + rand_toss + "! ... Got "
           + str(dict_coin_tosses['tot_heads']) + " head(s) so far and "
           + str(dict_coin_tosses['tot_tails']) + " tail(s) so far")
    return dict_coin_tosses


# Main Function
# Define the number of coint tosses and iterate
num_tosses = 5000
dict_coin_tosses = {
    'toss_number' : 0,
    'tot_heads' : 0,
    'tot_tails' : 0
}
print "__START OF COIN TOSSES__"
for toss in range(num_tosses):
    dict_coin_tosses = print_line(dict_coin_tosses)
print "__END OF COIN TOSSES__"
print ("___<><>     TOTAL PERCENT HEADS TO PERCENT TAILS  = "
       + str(round(float(dict_coin_tosses['tot_heads']) / num_tosses * 100, 1)) + "% : "
       + str(round(float(dict_coin_tosses['tot_tails']) / num_tosses * 100, 1)) + "%     <><>___")
       
