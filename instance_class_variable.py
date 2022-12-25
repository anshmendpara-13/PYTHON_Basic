class Employee:
    no_of_leaves = 8
    pass

ansh = Employee()
meet = Employee()

ansh.name = "Ansh"
ansh.salary = 5845
ansh.role = "instructor"

meet.name = "Meet"
meet.salary = 542
meet.role = "student"

print(meet.no_of_leaves)
print(Employee.no_of_leaves)
print(Employee.__dict__)
# Employee.no_of_leaves = 9
meet.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)
print(meet.no_of_leaves)
print(ansh.no_of_leaves)
