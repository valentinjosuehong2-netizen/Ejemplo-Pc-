import math
import random
import os
acumulador=100

def generar_numeros():
    a=random.randint(0,9)
    b=random.randint(0,9)
    c=random.randint(0,9)
    
    return 1,1,1

def restar(a,b):
    return a - b

def pozo(acc,valor):
    acc +=valor
    return acc 

def premio(a:int,b:int,c:int) ->bool:
    premio=False
    if a==b and b==c and a==c:
        premio=True
    return premio

repetir=True
numeros=0,0,0
tiene_premio=False
while repetir:

    # print(chr(94))
    # input()
    os.system("cls")
    numeros=generar_numeros()
    #numeros=(1,1,1)
    print(f"El pozo es de {acumulador}")
    print("{0:^3}{1:^3}{2:^3}".format(int(numeros[0]),int(numeros[1]),int(numeros[2])))
    tiene_premio=premio(*numeros)
    
    if tiene_premio:
    #if numeros[0]==numeros[1]==numeros[2]:
        mi_premio=acumulador * 80 / 100
        print("Ganaste",mi_premio)
        acumulador=restar(acumulador,mi_premio)
    else:
        acumulador=pozo(acumulador,5)           
    input()

    

