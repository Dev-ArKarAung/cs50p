class Student:
    def __init__(self, name, house):
        self.name = name 
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

def main():
    student = Student.get()
    print(student)


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

    # if I want to use property
    # @property
        # def name(self):
        #      return self._name
    
        # @name.setter
        # def name(self, name):
        #      if not name:
        #         raise ValueError("Missing name")
        #      self._name = name
    
        # @property
        # def house(self):
        #     return self._house
    
        # @house.setter
        # def house(self, house):
        #          if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        #               raise ValueError("Invalid house")
        #          self._house = house