words = "It's thanksgiving day. It's my birthday, too!"
print words.find("day")
words = words.replace("day", "month", 1)
print words

x = [2, 54, -2, 7, 12, 98]
min = min(x)
max = max(x)
print "The minimum is", min
print "The maximum is", max

my_list = ["hello", 2, 54, -2, 7, 12, 98, "world"]
my_new_list = [my_list[0], my_list[len(my_list)-1]]
print my_new_list

my_list = [19, 2, 54, -2, 7, 12, 98, 32, 10, -3, 6]
my_sorted_list = sorted(my_list)
my_sorted_list_1half = my_sorted_list[0:int(len(my_sorted_list)/2)]
my_sorted_list_2half = my_sorted_list[int(len(my_sorted_list)/2):len(my_sorted_list)]
my_new_sorted_list = my_sorted_list_2half.insert(0, my_sorted_list_1half)

print my_sorted_list
print my_sorted_list_1half
print my_sorted_list_2half
print my_new_sorted_list