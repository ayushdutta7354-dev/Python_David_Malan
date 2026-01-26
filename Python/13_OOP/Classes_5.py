# classes contd: raising error


class Student:
    def __init__(self, name, house,patronus, favsub):
        #if we dont pass name and house
        if not name:
            raise ValueError("Missing name")
        if house not in ["house 1", "house 2", "house 3"]:
            raise ValueError("Invalid House")

        self.name = name;
        self.house = house;
        self.patronus = patronus;
        self.favsub = favsub;
        # self is a parameter which is equal to the instance of clsses(objectes created)
    
    def __str__(self): #if i want my obj to behave like string, we have __str__
        # return "a student";
        return f"{self.name} from {self.house}";


    def charm(self):
        match self.patronus:
            case "Abhi":
                return "😊";
            case "Rahul":
                return "😶";
            case "Suresh":
                return "😎";
            case _:
                return "Nothing";


def main():
    student = get_student()
    student.favsub = "Electronics Engineering";#default value to change after user i/p.
    print(student);
    print(student.favsub);
    print(student.charm());


def get_student():
    name = input("enter name: ")
    house = input("enter house: ")
    patronus = input("enter patronus: ");
    favsub = input("enter favsub: ")
    # student = Student(name, house);
    return Student(name, house, patronus, favsub);


if __name__ == "__main__":
    main();


"""
We can import classes to other files.
we can create our own custom error: Eg: raise AyushError(".....")
"""