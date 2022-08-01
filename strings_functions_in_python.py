#len(s) vraca broj itemsa u objektu
x="rvc academy rvc academy rvc academy rvc academy"
len(x)
print(len(x))
#print(x.find('ac')) printa index od tog strigna
#print(x.upper())  #povecace sva slova
print(x.count("rvc",5,15))
""" da pobroji koliko puta se rvc nalazi u stringu
 ako startujemo od indexa 5 a zavrsimo sa 15 -printalo je 1"""

print(x.split()) #deli string krenuvsi od levo
print(x.strip("uklanja sve sto ne zelimo da prikaze"))
print(x.replace('rvc','pvc',3)) #da mi zameni onoliko puta koliko sam napisala,stari,novi i broj puta se upisuje