def arreglo(tamaño):
    articulos = []
    precios = []
    for i in range(tamaño):
        articulo = input('CAPTURE EL NOMBRE DEL PRODUCTO {}: '.format(i+1))
        print()
        precio = float(input('CAPTURA EL PRECIO DEL PRODUCTO {}: '.format(i+1)))
        print()
        articulos.append(articulo)
        precios.append(precio)
    return articulos, precios
def combinar_en_lista(articulos, precios):
    lista_combinada = []
    for j in range(len(articulos)):
        lista_combinada.append(articulos[j]) 
        lista_combinada.append(precios[j])    
    return lista_combinada
def imprimir():
    tamaño = int(input('CAPTURA EL TAMAÑO DE LOS ARREGLOS: '))
    articulos, precios = arreglo(tamaño)
    lista_combinada = combinar_en_lista(articulos, precios)
    print('\n----LISTA COMBINADA DE PRODUCTOS Y PRECIOS----')
    print(lista_combinada)
imprimir()
