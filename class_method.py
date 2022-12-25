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

ansh = Employee("Ansh",5845,"instructor")
meet = Employee("Meet",547,"student")

# ansh.change_leaves(54)

print(meet.printdetails())
# print(ansh.salary)
# print(ansh.no_of_leaves)
# print(meet.printdetails())
