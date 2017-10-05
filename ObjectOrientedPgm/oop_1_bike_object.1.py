# define object Bike
class Bike(object):
    def __init__(self, bike_make, color, price, max_speed):
        self.bike_make = bike_make
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayinfo(self):
        # print "Bike: " + self.color[0].upper() + self.color[1:] + " " + self.bike_make
        # print "Price: " + str(self.price)
        # print "Max Speed: " + str(self.max_speed) + " mph"
        # print "Total Miles Travelled: " + str(self.miles)

        # attrs = vars(self)
        # print ', '.join("%s: %s" % item for item.upper() in attrs.items())

        for attr, value in sorted(self.__dict__.iteritems()):
            print key_no_line(attr.upper()), ":", value
        return self
    def ride_forward(self):
        print self.color[0].upper() + self.color[1:], self.bike_make, "Riding forward >>>>"
        self.miles += 10
        # print "Total Distance Traveled (miles) =", self.miles
        return self
    def ride_reverse(self):
        print self.color[0].upper() + self.color[1:], self.bike_make, "Going Backwards <<<<"
        self.miles -= 5
        self.no_neg_miles()
        # print "Total Distance Traveled (miles) =", self.miles
        return self
    def no_neg_miles(self):
        # place a method on the object such that total miles travelled
        # cannot be less than 0
        if self.miles < 0:
            self.miles = 0
        return self

def key_no_line(key):
    # return the key name without any underscores
    # replace with spaces
    return key.replace("_", " ")

# create 3 instances of Bike object
bike_instances = [
    Bike('Schwinn', 'yellow', 250, 25),
    Bike('Huffy', 'grey', 150, 19),
    Bike('Trek', 'red', 550, 35)
]

bike_instances[0].ride_forward().ride_forward().ride_forward().ride_reverse().displayinfo()
bike_instances[1].ride_forward().ride_forward().ride_reverse().ride_reverse().displayinfo()
bike_instances[2].ride_reverse().ride_reverse().ride_reverse().displayinfo()