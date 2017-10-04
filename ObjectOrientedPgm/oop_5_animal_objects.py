class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def display_health(self):
        print self.name[0].upper() + self.name[1:] + " health: " + str(self.health)
        return self

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon!!"
        return self


# MAIN PROGRAM
# generate new animals
cat = Animal('cat')
horse = Animal('horse')
elephant = Animal('elephant')
dog = Dog('dog')
dragon = Dragon('dragon')

# walk and run
cat.walk().display_health()
horse.run().display_health()
elephant.walk().run().walk().display_health()
dog.walk().walk().walk().run().run().pet().display_health()
dragon.run().run().fly().fly().display_health()