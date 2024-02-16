# -*- coding: utf-8 -*-
"""
Haz el algoritmo de Euclides

"""

def MCD(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        temp = b
        b = a % b
        a = temp
        return MCD(a,b)

print(MCD(270,192))    
