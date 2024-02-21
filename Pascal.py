# -*- coding: utf-8 -*-
"""
triangulo de pascal
"""

def calcular_coeficientes(n):
    coeficientes = [[1]]
    for i in range(1, n):
        fila_anterior = coeficientes[-1]
        nueva_fila = [1]
        for j in range(1, i):
            nueva_fila.append(fila_anterior[j - 1] + fila_anterior[j])
        nueva_fila.append(1)
        coeficientes.append(nueva_fila)
    return coeficientes

def imprimir_piramide_pascal(n):
    coeficientes = calcular_coeficientes(n)
    max_width = len(' '.join(map(str, coeficientes[-1])))
    for fila in coeficientes:
        fila_str = ' '.join(map(str, fila)).center(max_width)
        print(fila_str)

imprimir_piramide_pascal(6)
