x=10
y="training"
z=[10,20,30,40,50]
#liste mogu da sadrze razlciite data tipove, ili integer ili string
b=["st", "tr", "tr"]
c=[1,"string",50.1]

#listi se pristupa kroz indexe
#indexi krecu od 0
print(b[0])
print(c[2])
print(b[0:2])

#list.append(x) - dodaj item na ennd liste
#list.insert(i,x) -insert item on given positions
#list.remove(x) remove first item from the list  whose value is x
#list.clear(x)
#list.pop([i]) -remove items on particular index
#https://docs.python.org/3/

cities=["Beograd","Kragujevac","Novi Sad"]
cities.append("Nis")
print(cities)

cities.insert(1,"Cacak")
print(cities)

cities.remove("Nis")
print(cities)

cities.pop(1)
print(cities)
