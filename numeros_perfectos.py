# -*- coding: utf-8 -*-
"""

números perfectos
"""

def esPerfecto(a):
    arreglo = []
    valor = 0
    for i in range(1,int((a / 2) + 1)):
        if(a % i == 0):
            arreglo.append(i)
    for j in range(0, len(arreglo)):
        valor = valor + arreglo[j]

    if(valor == a):
        return True
    else:
        return False


def buscarPerfectos(a):
    for i in range(1,a):
        if(esPerfecto(i)):
            print(i)
            
buscarPerfectos(500)        