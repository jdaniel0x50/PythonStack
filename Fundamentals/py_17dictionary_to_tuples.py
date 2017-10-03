my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def create_tuple(key, value):
    return (key, value)

# Main Program
# Cyle through the keys in the dictionary and 
# pass the key, value pair to a function to create a tuple
new_list = []
for key, value in my_dict.iteritems():
    new_tuple = create_tuple(key, value)
    new_list.append(new_tuple)

print new_list