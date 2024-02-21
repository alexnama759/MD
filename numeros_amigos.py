# -*- coding: utf-8 -*-
"""
encontrar números amigos
"""

def sonAmigos(a,b):
    valores = []
    valores2 = []
    valorA = 0
    valorB = 0
    for i in range(1,int((a / 2) + 1)):
        if(a % i == 0):
           valores.append(i)
    for j in range(1,int((b / 2) + 1)):
        if(b % j == 0):
           valores2.append(j)
           
           
    for k in range(0,len(valores)):
        valorA =  valorA + valores[k]
    for l in range(0,len(valores2)):
        valorB = valorB + valores2[l]
    
    if(valorA == b and valorB == a):
        print("Son números amigos")
    else:
        print("No son números amigos")
        
        
        
sonAmigos(220,284)        