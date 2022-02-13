class Fruit(object):

    def factory(type):
        if type == "Peach":
            return Peach()
        if type == "orange":
            return orange()

    factory = staticmethod(factory)

class Peach(Fruit):
    def drive(self):
        print("The Fruit that is picked is a peach")

class orange(Fruit):
    def drive(self):
        print("The Fruit that is picked is a orange")

# Create object using factory.
obj = Fruit.factory("Peach")
obj.drive()