def calcular_agua(cant_inicialagua, num_generacion):
    if num_generacion > 50:
        return "El número máximo para las generaciones debe ser de 50."
    
    num_organismos = 1 
    agua_actual = cant_inicialagua
    
    for generacion in range(num_generacion):
        agua_actual /= num_organismos 
        num_organismos *= 2 
    
    return agua_actual

cant_inicialagua = float(input("Inserta la cantidad inicial de agua: "))
num_generacion = int(input("Inserta el número de generaciones (máximo 50): "))

if num_generacion <= 50:
    agua_por_organismo = calcular_agua(cant_inicialagua, num_generacion)
    print(f"La cantidad de agua por organismo después de {num_generacion} generaciones es de {agua_por_organismo} ltrs.")
else:
    print("El número máximo para las generaciones debe ser de 50.")
