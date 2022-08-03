class Employee: #define first class
    def __init__(self,fname,lname,email):
        self.fname=fname
        self.lname=lname
        self.email=email
    def greet_person(self): #define first method
        print("Hello welcome " + self.fname)

emp1= Employee("Mari","Andric","marijana@mindnow.io") # dve instance klase employee
emp2=Employee("Leni","Andric", "leni@mindnow.io")
emp3=Employee("Mika","Lndric", "leni@mindnow.io")
emp4=Employee("Pera","Kndric", "leni@mindnow.io")
emp5=Employee("Laza","Bndric", "leni@mindnow.io")


print(emp1.fname)
print(emp2.fname)
emp2.greet_person()
emp4.greet_person()


