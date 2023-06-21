
'''
nome = input ("Inserire il nome: ")
anni = input ("Inserire gli anni: ")


print (nome, "ha", anni, "anni e tra 10 anni avrai" , int(anni) +10, "anni")
'''

''' 
user = input ("Inserire il user: ")
pswd = input ("Inserire la pswd: ")

if user == "rossi" and pswd == "ciao123":
    print("Login effettuato con successp!")
elif user == "rossi" and pswd != "ciao123":
    print ("pswd errata")
elif user != "rossi" and pswd == "ciao123":
    print("user errato")
else:
    print("accesso negato!, user e pswd erratti")
'''
'''
lista = []

lista.append ("Aniello")
lista.append ("D'Angelo")
lista.append (18)
lista.append ("Novembre")
lista.append (1977)

print (lista)

print (lista.index("Novembre"))

print (lista.count(18))

'''


'''
base = input ("Inserire la base : ")
altezza = input ("Inserire l'altezza : ")

print ("Perimetro: ", ( int(base) + int(altezza) ) *2 )
print ("Area: ", int(base) * int(altezza) )

'''

'''
Valore1 = int ( input ("Inserire Valore 1: "))
Valore2 = int (input ("Inserire Valore 2: "))

print ("Somma ", Valore1, "+", Valore2 , "=" , Valore1 + Valore2 )
print ("Prodotto  ", Valore1, "*", Valore2 , "=" , Valore1 + Valore2 )

'''

'''
Valore1 = int ( input ("Inserire Valore 1: "))
Valore2 = int (input ("Inserire Valore 2: "))
Valore3 = int (input ("Inserire Valore 3: "))

if Valore1 > Valore2:
    if Valore1 > Valore3:
        print ("il più grande è Valore1", Valore1)
    else:
        print("il più grande è Valore2", Valore3)
else:
    if Valore2 > Valore3:
        print("il pirù grande è Valore2", Valore2)
    else:
        print("il pirù grande è Valore3", Valore3)

'''

Valore1 = int ( input ("Inserire Valore 1: "))
Valore2 = int (input ("Inserire Valore 2: "))
Valore3 = int (input ("Inserire Valore 3: "))

print (Valore1,Valore2,Valore3)

if Valore1 > Valore2:
    tmp= Valore1
    Valore1= Valore2
    Valore2= tmp

if Valore1 > Valore3:
    tmp= Valore1
    Valore1= Valore3
    Valore3= tmp

if Valore2 > Valore3:
    tmp= Valore2
    Valore2= Valore3
    Valore3= tmp

print (Valore1,Valore2,Valore3)