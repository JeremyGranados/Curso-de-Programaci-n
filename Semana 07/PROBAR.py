# =====================================================================
# CÓDIGO DE practica de asistencia
# =====================================================================

# Asistencia reporte
Cantidad = 15

nombre_estudiante = input("Ingrese tu nombre: ")
asistencia = int(input("Ingrese la cantidad de asistencias: "))

if asistencia < 0:
    print("La cantidad de asistencias no puede ser negativa.")
elif asistencia >= Cantidad:
    print(f"{nombre_estudiante} ha aprobado.")
else:
    print(f"{nombre_estudiante} no ha aprobado.")