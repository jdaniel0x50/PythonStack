# define object Car
class Car(object):
    def __init__(self, car_make, color, price, max_speed, fuel_level, fuel_mileage):
        self.car_make = car_make
        self.color = color
        self.price = price
        self.max_speed = max_speed
        self.fuel_level = fuel_level
        self.fuel_mileage = fuel_mileage
        self.tax_rate = self.taxes()
    def displayinfo(self, i):
        print "___ CAR # " + str(i+1) + "___"
        for attr, value in sorted(self.__dict__.iteritems()):
            print key_no_line(attr.upper()), ":", value
        return self
    
    def taxes(self):
        # determine the tax percentage based on price
        if self.price < 10000:
            return 0.15
        else:
            return 0.12

def key_no_line(key):
    # return the key name without any underscores
    # replace with spaces
    return key.replace("_", " ")

# create 6 instances of Car object
car_instances = [
    Car('Ford', 'blue', 2000, '35mph', 'Full', '25mpg'),
    Car('Subarua', 'orange', 2000, '55mph', 'Not Full', '40mpg'),
    Car('Honda', 'red', 2000, '45mph', 'Kind of Full', '30mpg'),
    Car('Toyota', 'blue', 2000, '48mph', 'Full', '38mpg'),
    Car('Buick', 'silver', 2000, '50mph', 'Empty', '24mpg'),
    Car('Chevy', 'green', 2000, '40mph', 'Full', '22mpg')
]

for i in range(0,len(car_instances)):
    car_instances[i].displayinfo(i)
