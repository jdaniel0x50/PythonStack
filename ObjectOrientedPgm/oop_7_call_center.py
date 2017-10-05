# time module needed to handle time of call
# random module used to generate random calls
from datetime import time
import random

class Call(object):
    def __init__(self, caller_name, caller_phone, call_time, call_reason):
        self.id = id(self)
        self.caller_name = caller_name
        self.caller_phone = caller_phone
        self.call_time = call_time
        self.call_reason =  call_reason
    def display_call(self):
        # method prints all attributes and values
        print "___ CALL INFORMATION (" + self.caller_name + ") ___"
        for attr, value in sorted(self.__dict__.iteritems()):
            # call external function to remove _ from attribute name
            print key_no_line(attr.upper()), ":", value
        return self

class CallCenter(object):
    def __init__(self, size):
        self.calls = []
        self.queue_size = size
    def add_call(self, caller_name, caller_phone, call_time, call_reason):
        if len(self.calls) > self.queue_size:
            queue_size_error()
            return -1
        self.calls.append(Call(caller_name, caller_phone, call_time, call_reason))
        return self
    def remove_first_call(self):
        # removes the first call from the call list
        del self.calls[0]
        return self
    def remove_call_by_phone(self, phone_number):
        # removes a call based on phone number of caller from call list
        for call_obj in self.calls:
            if call_obj.caller_phone == phone_number:
                self.calls.remove(call_obj)
        return self
    def display_all_call_info(self):
        # displays full list of information about each call (all attributes)
        for call_obj in self.calls:
            call_obj.display_call()
        return self
    def queue_info(self):
        # displays info about all calls -- name and phone number for each call and length of the queue
        i = 1
        print "___ CALL QUEUE INFORMATION ___"
        for call_obj in self.calls:
            print_string = "Call #" + str(i) + " - "
            print_string += call_obj.caller_name + ", " + call_obj.caller_phone
            # if the minutes of the time is 00, force the program to write double 0
            if call_obj.call_time.minute == 0:
                minutes = '00'
            else:
                minutes = str(call_obj.call_time.minute)
            print_string += " - called at " + str(call_obj.call_time.hour) + ":" + minutes
            print print_string
            i += 1
        print "___ END OF QUEUE ___"
        print "___ TOTAL NUMBER OF CALLS IN QUEUE = " + str(i-1) + " ___"
        return self
    def queue_sort_time(self):
        # sorts calls in queue according to time of call
        for i in range(len(self.calls)):
            for j in range(i+1, len(self.calls)):
                if self.calls[i].call_time > self.calls[j].call_time:
                    temp_store = self.calls[i]
                    self.calls[i] = self.calls[j]
                    self.calls[j] = temp_store
        return self


def key_no_line(key):
    # return the key name without any underscores
    # replace with spaces
    return key.replace("_", " ")

def queue_size_error():
    print "The call center cannot accept any more calls!"
    print "The queue is full. This call has not been entered."
    print "Please close out and remove calls from the queue before proceeding."

# instantiate new calls using random list generators
# random list of 30 names
names_list = [
    'Yasuko Mcglown',
    'Bart Tompson',
    'Williemae Ashmore',
    'Jona Ullery',
    'Belle Mcguire',
    'Kelli Odonoghue',
    'Billy Drummond',
    'Carlita Wiles',
    'Marianne Peete',
    'Carmelita Durocher',
    'Fernando Whitton',
    'Andree Willis',
    'Colette Gaudet',
    'Lionel Leininger',
    'Nancy Rollison',
    'Georgina Teixeira',
    'Kaley Lukes',
    'Kamilah Mcpeak',
    'Lance Tower',
    'Dolores Anding',
    'Danette Findlay',
    'Tanner Dipasquale',
    'Berry Lintner',
    'Lauralee Trumbo',
    'Josephine Cushing',
    'Drema Pottinger',
    'Sommer Tingey',
    'Sherrill Poat',
    'Jinny Peiffer',
    'Louie Pillai'
]
# random list of 15 phone numbers
phone_numbers = [
    '(389) 271-7065',
    '(333) 576-0239',
    '(242) 801-9160',
    '(404) 146-2665',
    '(365) 324-6734',
    '(131) 787-6917',
    '(292) 321-2520',
    '(947) 993-9469',
    '(993) 768-2436',
    '(747) 887-7546',
    '(189) 293-1704',
    '(623) 636-0372',
    '(614) 416-7458',
    '(244) 814-4100',
    '(145) 943-4876'
]
# random list of 15 times
times_list = [
    time(8, 10),
    time(9, 15),
    time(9, 45),
    time(10, 00),
    time(10, 30),
    time(11, 15),
    time(12, 15),
    time(12, 40),
    time(13, 20),
    time(14, 25),
    time(15, 50),
    time(17, 00),
    time(17, 20),
    time(17, 35),
    time(17, 40),
    time(18, 00),
    time(18, 30),
    time(19, 30),
    time(19, 40),
    time(19, 55)
]
# random list of call reasons
call_reasons = [
    'question',
    'new account',
    'support',
    'complaint'
]

# generate call center
my_call_center = CallCenter(50)

# generate random calls
num_calls = 10
for i in range(10):
    obj_create = my_call_center.add_call(
        names_list[random.randint(0, len(names_list)-1)],
        phone_numbers[random.randint(0, len(phone_numbers)-1)],
        times_list[random.randint(0, len(times_list)-1)],
        call_reasons[random.randint(0, len(call_reasons)-1)]
        )
    # if the __init__ method returns -1, there was queue size error; break
    if obj_create == -1:
        break

# view all call information for calls in queue at the call center
# my_call_center.display_all_call_info()

# remove the first call from the call center and display queue 
# my_call_center.queue_info().remove_first_call().queue_info()

# remove call instance from call center by phone number
# used to get phone number to remove
# phone_to_remove = my_call_center.calls[7].caller_phone
# my_call_center.queue_info().remove_call_by_phone(phone_to_remove).queue_info()


# apply sorting function to sort by time of call
my_call_center.queue_info().queue_sort_time().queue_info()
