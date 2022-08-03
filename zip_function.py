list1= ["India", "USA", "Australia","UK"]
list2= ["Pune","New York", "Sydney", "London"]
#s=zip(list1,list2)
#print(list(s))

total_cost=[45,46,47]
sale_price=[50,51,52]

for x,y in zip(total_cost,sale_price):
    print(y-x)

cities=[["india","delhi"], ["Australia","Melburn"],["Canada","Vancuver"]]
for country,city in cities:
    print("country is "+country+" and city is "+ city)

my_dictionary= dict(cities)
print(my_dictionary)
for country,city in my_dictionary.items():
    print(country,city)