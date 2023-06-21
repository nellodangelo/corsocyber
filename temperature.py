

temperature = []

print ("Inserire le temperature")
print ("Inserire x per uscire")

num = -1
contatore=0

while num != 0:
    num = int(input("Inserire valore: "))
    if num!=0:
        contatore += 1
        temperature.append(num)

print ("")

for i in temperature:
    print ("Temperature: ", i)

somma = 0
for i in temperature:
    somma += int(i)

print ("La media è ", somma/contatore)