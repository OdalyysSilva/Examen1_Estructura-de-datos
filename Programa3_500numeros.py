import numpy as np
import time

elementos_lista= int(input("Ingrese cuantos datos requieres (minimo 500): "))
lista=np.random.randint(0,101, size=( elementos_lista))
np.set_printoptions(threshold=np.inf, linewidth=np.inf, suppress=True)

buscar_numero= int(input("Ingrese un número en especifico que desee buscar: "))
print(lista)

print(" Busqueda lineal ")
empezar_tiempo= time.time()
indices = np.where(lista == buscar_numero)
if indices[0].size > 0:
    print(f"Elemento encontrado en el índice {indices[0][0]}")
else:
    print("Elemento no encontrado")
terminar_tiempo=time.time()
tiempo= terminar_tiempo - empezar_tiempo
print(f"\nLa busqueda lineal tardo {tiempo}s en ejecutarse")

lista_ordenada = np.sort(lista)
print("Lista ordenada:", lista_ordenada)

print("Búsqueda binaria")
empezar_tiempo2= time.time()
indice = np.searchsorted(lista_ordenada, buscar_numero)
if indice < len(lista_ordenada) and lista_ordenada[indice] == buscar_numero:
    print(f"Elemento encontrado en el índice {indice} de la lista ordenada")
else:
    print("Elemento no encontrado")
terminar_tiempo2=time.time()
tiempo2= terminar_tiempo2 - empezar_tiempo2
print(f"\nLa busqueda binaria tardo {tiempo}s en ejecutarse")













        

