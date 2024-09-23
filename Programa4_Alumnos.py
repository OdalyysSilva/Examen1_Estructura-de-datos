class Estudiante:

    def agregar_estudiante(self, arreglo, nombre):
        if nombre in arreglo:
            print(f"{nombre} ya está en la lista.")
        else:
            arreglo.append(nombre)
            print(f"{nombre} ha sido agregado al arreglo.")
    
    def busquedaA(self, arreglo1, arreglo2):
        if not arreglo1:  # Condición base: arreglo1 vacío
            return []
        if arreglo1[0] not in arreglo2:
            return [arreglo1[0]] + self.busquedaA(arreglo1[1:], arreglo2)
        else:
            return self.busquedaA(arreglo1[1:], arreglo2)

    def busquedaB(self, arreglo2, arreglo1):
        if not arreglo2:  # Condición base: arreglo2 vacío
            return []
        if arreglo2[0] not in arreglo1:
            return [arreglo2[0]] + self.busquedaB(arreglo2[1:], arreglo1)
        else:
            return self.busquedaB(arreglo2[1:], arreglo1)

    def busqueda_comun(self, arreglo1, arreglo2):
        if not arreglo1:  # Condición base: arreglo1 vacío
            return []
        if arreglo1[0] in arreglo2:
            return [arreglo1[0]] + self.busqueda_comun(arreglo1[1:], arreglo2)
        else:
            return self.busqueda_comun(arreglo1[1:], arreglo2)


my_object = Estudiante()


arreglo1 = []
arreglo2 = []


for i in range(10):
    nombre1 = input(f"Ingrese el nombre del estudiante para arreglo1 ({i+1}): ")
    nombre2 = input(f"Ingrese el nombre del estudiante para arreglo2 ({i+1}): ")
    my_object.agregar_estudiante(arreglo1, nombre1)
    my_object.agregar_estudiante(arreglo2, nombre2)


print("Estudiantes en arreglo1 que no están en arreglo2:", my_object.busquedaA(arreglo1, arreglo2))
print("Estudiantes en arreglo2 que no están en arreglo1:", my_object.busquedaB(arreglo2, arreglo1))
print("Estudiantes comunes en ambos arreglos:", my_object.busqueda_comun(arreglo1, arreglo2))


        


        
    
        