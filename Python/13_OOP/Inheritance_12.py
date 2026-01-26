# Inheritance 2:


class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


ayush = Vault(30, 55, 45)
ramesh = Vault(42, 20, 75)

print(ayush)
print(ramesh)

total = ayush + ramesh;
print(total)

"""
operator overloading: when you can use one operator for another task, not just the conventn task.
"""
