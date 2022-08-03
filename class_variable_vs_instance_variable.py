class RateOfInterest:
    interest=0.06  #class variable
    def __init__(self,name,loan,interest):
        self.name=name
        self.loan=loan
      # self.interest=interest  #instance variables
 #kada def class instance - ne treba nam ovde ova variable instanca
    def calculate_interest(self):
        print("Total interest: ", self.loan *self.interest)


p1=RateOfInterest('Marijana', 5000,0.03)
p1.calculate_interest()

p2=RateOfInterest("Nemanja",56000,0.03)
p2.calculate_interest()