import random


class Hat:
    # def __init__(self): we dont need this bcz we dont create any insatnce of Hat class.
    #     self.houses = ["house 1","house 2","house 3","house 4","house 5"];

    houses = ["house 1", "house 2", "house 3", "house 4", "house 5"]

    @classmethod
    def sort(cls, name):  # cls pints to class itself (class Hat())
        print(name, "is in", random.choice(cls.houses))
        return 0


# now i dont need to instantiate an object in order to acess sort method.

Hat.sort("Ayush")


# nex lec