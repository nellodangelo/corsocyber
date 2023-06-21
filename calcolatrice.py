
print ("")
Valore1 = int (input ("Inserire Valore 1: "))
Valore2 = int (input ("Inserire Valore 2: "))

print ("")
print ("Selezionare l'operazione da eseguire:")
print ("1 - sommma")
print ("2 - sottrazione")
print ("3 - moltiplicazione")
print ("4 - divisione")
print ("")

operazione  = input ("scelta: ")

match operazione:
    case "1":
         print (f"Somma: {Valore1} + {Valore2} =", Valore1 + Valore2 )
    case "2":
         print (f"Sottrazione: {Valore1} - {Valore2} =", Valore1 - Valore2 )
    case  "3":
         print (f"Moltiplicazione: {Valore1} * {Valore2} =", Valore1 * Valore2 )
    case  "4":
         print (f"Divisione: {Valore1} / {Valore2} =", int(Valore1 / Valore2) )
    case _:
        print ("scelta errata")