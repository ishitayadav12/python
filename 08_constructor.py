class Employee:
    company= "Google"

    def __init__(self, name, salary, position):
        self.name = name
        self.salary = salary
        self.position = position
        print("Employee is created")

    def getDetails(self):
        print(f"Name of employee is {self.name}")
        print(f"Salary of employee is {self.salary}")
        print(f"Role of employee is {self.position}")
    
    def getSalary(self):
      print(f"Salary for this emplyee working in company {self.company} is {self.salary} \n")

    @staticmethod
    def greet():
      print("Goodmorning, sir/madam")

ishita=Employee("Ishita" , 1000000, "SoftwareDeveloper")
ishita.getDetails()

# solution
# storing info of programmer working at microsoft

class programmer:
    complany="Microsoft"

    def __init__(self, name, age, salary, contact, adress):
        self.name=name
        self.age=age
        self.salary=salary
        self.contact=contact
        self.adress=adress
         
    def getInfo(self):
        print(f"Name of employee: {self.name} \n age of employee: {self.age} \n salary of employee: {self.salary} \n contact details of employee: {self.contact} \n ")

ishita=programmer("ishita",20, 200000, 9958397709, "234 chennai")
harry=programmer("harry", 40, 435033, 489275926, "332 london")

ishita.getInfo()
harry.getInfo()


# designing a calculator
class calculator:
    def __init__(self,num):
        self.num=num

    def square(self):
        print(f"Sqaure of {self.num} is {self.num **2}")
    def cube(self):
        print(f"Cube of {self.num} is {self.num **3}")
    def squareroot(self):
        print(f"Sqaure Root of {self.num} is {self.num **0.5}")

a=calculator(int(input("User enter number")))
a.square()
a.cube()
a.squareroot()
    
