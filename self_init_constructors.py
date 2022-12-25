import self as self


class Employee:
    no_of_leaves = 8
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary} and Role is {self.role}"

ansh = Employee("Ansh",5845,"instructor")
# meet = Employee()

# ansh.name = "Ansh"
# ansh.salary = 5845
# ansh.role = "instructor"
#
# meet.name = "Meet"
# meet.salary = 542
# meet.role = "student"

print(ansh.printdetails())
print(ansh.salary)