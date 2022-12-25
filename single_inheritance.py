import self as self

class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary} and Role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves = newleaves

    @staticmethod
    def printgood(string):
        print("my name is " + string)
        return 13

    @classmethod
    def from_str(cls, string):
        # params = string.split("-")
        # return cls(params[0], params[1], params[2])
        return cls(*string.split("-"))

class Programmer(Employee):
    def __init__(self, aname, asalary, arole, languages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.languages = languages


    def printprog(self):
        return f"The Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are {self.languages}"

# ansh = Employee("Ansh",5845,"instructor")
# meet = Employee("Meet",547,"student")
ansh = Programmer("ansh",555,"prongrmmer",["python","c++"])
# print(ansh.printprog)
print(ansh.printprog())