# Inheritance:


# 3. wizard is the parent class of Student and Professor.
class Wizard: 
    def __init__(self, name):
        if not name:
            raise ValueError("Missing Name");
        self.name = name;


# 1.
class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name);
        self.house = house;
    ...


# 2.
class Professor(Wizard):
    def __init__(self, name, subject):
         super().__init__(name);
         self.subject = subject;
    ...


wizard = Wizard("David Malan");
ayush = Student("Ayush Dutta", "House 3");
abhi = Professor("Abhi", "IT");

print(ayush);
print(abhi);