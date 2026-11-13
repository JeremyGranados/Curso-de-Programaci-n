#Calcular la edad del usuario
edad = 0

Mes = int(input("Ingrese el mes en que nació (1-12): "))
try:
    if Mes < 1 or Mes > 12:
        raise ValueError("El mes ingresado no es válido. Debe estar entre 1 y 12.")
except ValueError as e:
    print(e)
    exit()
Dia = int(input("Ingrese el día en que nació: "))

Anio = int(input("Ingrese el año en que nació: "))

edad = 2026 - Anio
print("su edad es:", edad, "años.")

# Indicar cuanto dias tiene de estar viviendo
cantidad_dias = (2026 - Anio) * 365 + (Mes - 1) * 30 + Dia
print("Usted ha vivido aproximadamente", cantidad_dias, "días.")

#Calcular cuantos años va a tener en 5 años
edad_actual = edad
edad_en_5_anios = edad_actual + 5
print("Usted tendrá", edad_en_5_anios, "años en 5 años.")


# Si tiene hijos a cierta edad, indicar cuantos años tiene cada hijo
hijos = int(input("Ingrese la edad que le gustaria tener un hijo: "))
anio_hijo = int(input("colocar un año y saber cuántos años tendría su hijo: "))
hijos_edad = anio_hijo - (Anio + hijos)

if hijos_edad < 0:
    print("El hijo aún no ha nacido.")
elif hijos_edad == 0:
    print("Su hijo nacerá este año.")
else:
    print("Su hijo tendría", hijos_edad, "años.")