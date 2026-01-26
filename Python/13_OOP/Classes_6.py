# Properties and decorators:

class Student:
    def __init__(self, name, house, petronus):
        if not name:
            raise ValueError("Missing name");
        self.name = name;
        self.house = house;
        self.petronus  = petronus;

    def __str__(self):
        return f"{self.name} from {self.house}, the petronus is {self.petronus}";


    @property
    def name(self):
        return self._name;

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("missing Name");
        self._name = name;

    @property
    def house(self):
        return self._house;

    @house.setter
    def house(self, house):
        if house not in ["house 1","house 2", "house 3","house 4", "house 5"]:
            raise ValueError("Invalid house");
        self._house = house;

    def charm(self):
        match self.petronus:
             case "Abhi":
                return "😊";
             case "Rahul":
                return "😶";
             case "Suresh":
                return "😎";
             case _:
                return "Nothing";


def main():
    student = get_student();
    # student.house = "house 6";
    print(f"{student.name} from {student.house}, petronus {student.petronus}");

def get_student():
    name = input("Enter name: ");
    house = input("Enter house: ");
    petronus = input("Enter petronus: ");
    return Student(name,house,petronus);

if __name__ == "__main__":
    main();
