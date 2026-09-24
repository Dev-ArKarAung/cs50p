class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name 
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    



def main():
    student = get_student()
    print(student)

def get_student():
    name = input("Name:")
    house = input("House: ")
    return Student(name, house)



if __name__ == "__main__":
    main()




#def get_student():

    #storing attri in class normal way 
    # student = Student()
    # student.name = input("Name: ")
    # student.house = input("House: ")
    # return student


    # name = input("Name: ")
    # house = input("House: ")
    # return [name, house] for list# (name, house) for tuple
    # return {"name": name, "house": house} compact dict in a single line

    # Dict normal way
    # student = {}
    # student["name"] = input("Name: ")
    # student["house"] = input("House: ")
    # return student



    # if want to add charm
    # def charm(self):
        #     match self.patronus:
        #         case "Stag":
        #             return "🐴"
        #         case "Otter":
        #             return "🦦"
        #         case "Jack Russell terrier":
        #             return "🐶"
        #         case _:
        #             return "🪄"