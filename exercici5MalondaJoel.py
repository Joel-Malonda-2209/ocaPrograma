import random


caselles = int(input("Dis-me equantes caselles té el tauler: "))
cont = 0
posicio = 0

print("Estic en la casella 0")

while posicio < caselles:
   
    dau= random.randint(1, 6)

    
    posicio = posicio + dau
    print("He tret un ",dau, "i estic en la casella", posicio)
    cont = cont + 1
    if posicio % 5 == 0:
        posicio += 5
        print("D'oca en oca i tire perque em toca, estic en la casella", posicio)
    

    if posicio == caselles:
        break


print("He guanyat amb un total de", cont, "tirades")
    
