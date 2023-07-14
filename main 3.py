# WF inputs da 1 a 1000
# if pari prende radice quadrata arrotondata verso l'alto all'intero più vicino
# if dispari prende la radice
# calcolare la somma dei numeri da 1 a 1000

import math


def WF(i):
    s = 0
    while i <= 1000 :
        x = i
        print("------------- ")
        print("Il valore di i è " + str(i))
        if x % 2 == 0 :
            x = round(math.sqrt(x), 0)
            print("If - La radice di x approx è " + str(x))
            s = s + x
            print("La somma è " + str(s))
            i += 1
        else :
            x = x ** 2
            print("Else - Il quadrato di x è " + str(x))
            s = s + x
            print("La somma è " + str(s))
            i += 1
    print(s)
