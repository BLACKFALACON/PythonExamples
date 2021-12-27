# Public Members
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self): 
        print("Name: ", self.name, 'Salary:', self.salary)

emp = Employee('Jessa', 10000)


print("Name: ", emp.name, 'Salary:', emp.salary)
emp.show()


#Private Members
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary


emp = Employee('Jessa', 10000)
print('Name:', emp.name)
print('Salary:', emp._Employee__salary)


#Protected Member

class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"

class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)

    def show(self):
        print("Employee name :", self.name)
        print("Working on project :", self._project)

c = Employee("Jessa")
c.show()

# Direct access protected data member
print('Project:', c._project)


#Getters and Setters

class Student:
    def __init__(self, name, age):
        # private member
        self.name = name
        self.__age = age

    # getter method
    def get_age(self):
        return self.__age

    # setter method
    def set_age(self, age):
        self.__age = age

stud = Student('Jessa', 14)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())

# changing age using setter
stud.set_age(16)

# retrieving age using getter
print('Name:', stud.name, stud.get_age())