class TestPython:   #konstruktor
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def calculate(self): # metoda
        return self.l*self.b


test1=TestPython(3,5)  #objekti u pajtonu
test2=TestPython(5,6)
print(test1.calculate()) # ova calulate metoda je pozvana na test1 objektu
print(test2.calculate())