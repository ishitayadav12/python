#  classes and objects
class Employee:
    

    def __init__(self,name, company):
      self.name=name
      self.company=company
  
  
    def getSalary(self):
      print(f"Salary for employee {self.name} working in company {self.company} is {self.salary}")

    @staticmethod
    def greet():
      print("Goodmorning, sir/madam")

ishita= Employee("ishita", "GOOGLE")
amisha= Employee("amisha", "Microsoft")


ishita.salary=400000
ishita.getSalary()
ishita.greet()
amisha.salary=600000
amisha.getSalary()
amisha.greet()
