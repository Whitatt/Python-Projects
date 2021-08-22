
class Fish:#created fish class with init method, populate fname and lname class variables for each fish object/subclass
    def __init__(self, first_name, last_name="fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):#added methods swim/backwards to class so that every subclass will also be able to make use of methods.
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")

class Trout(Fish):#created child class and provided methods
    pass

terry = Trout("Terry")
print(terry.first_name + " " + terry.last_name)
print(terry.skeleton)
print(terry.eyelids)
terry.swim()
terry.swim_backwards()

class Clownfish(Fish):#provided additonal child class with methods

    def live_with_anemone(self):
        print("The clownfish is coexisting with the sea anemone.")

casey = Clownfish("casey")
print(casey.first_name + " " + casey.last_name)
casey.swim()
casey.live_with_anemone()


class Family:
    # Parent class constructor
    def __init__(self, name):
        self.name = name

# father class inherited from Family
class Father(Family):
    #child class constructor
    def __init__(self, name, age):
        #parent class constructor called from child class
        Family.__init__(self, name)
        self.age = age

f = Father("David", 50)
print(f.name)
print(f.age)

class Mother(Family):#repeated father class and replaced with mother class
    def __init__(self, name, age):
        Family.__init__(self,name)
        self.age = age

m = Mother("Mary", 48)
print(m.name)
print(m.age)


