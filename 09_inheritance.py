# single inheritance

class Employee:                                          #base class
    company="Google"
    def showDetails(self):
        print("This is an Employee og Google")

class programmer(Employee):                              #derived class
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        print(f"Your details are: {self.name}\n {self.salary}")

p=programmer("Ishita" , 300000)
p.showDetails()


# multiple inheritance

class customer:                                        #parent class
    company= "Visa"
    eCode=120

class retailer:                                        #parent class
    company= "File"
    level=0
    
    def upGradeLevel(self):
        self.level= self.level + 2

class dealer(customer,retailer):                      #child class
    name="rahul"

p=dealer()
p.upGradeLevel()
print(p.level)
    


# multilevel inheritance

class person:                                            #parent class
    country="India"

    def takeBreak(self):
        print("Take a break \n")

class company(person):                                   #child 1
    company="Microsoft"

    def getSalary(self):
       print(f"Salary is : {self.salary} \n ")


class program(company):                                  #child 2
    role="Coder"

    def defineRole(self):
        print(f"Your role is: {self.role}")

p = person()
p.takeBreak()
c = company()
c.takeBreak()
r = program()
print(c.company)

# solutions

class animals:
    animalType= "Wild"

class pet(animals):
    color= "White"

class dog(pet):
    @staticmethod
    def bark():
        print("Bow! Bow!")

d= dog()
d.bark()

# solution2

class employee:
    salary=100
    increment=1.5

    @property
    def salaryIncrement(self):
     return self.salary*self.increment

    @salaryIncrement.setter
    def salaryIncrement(self,sai):
        self.increment=sai/self.salary

e=employee()
print(e.salaryIncrement)

# solution 3

class complex:
    def __init__(self, r, i):
        self.real= r
        self.imaginary= i

    def __add__(self,c):
        return complex(self.real + c.real , self.imaginary + c.imaginary)

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

c1=complex(4,9) 
c2=complex(5,8)
print(c1+c2)




    



