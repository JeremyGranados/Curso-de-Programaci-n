# =====================================================================
# CÓDIGO DE PRÁCTICA: Cálculo de Promedio y Análisis de Ventas en V.S. Code
# =====================================================================

# Lista que almacena las ventas de las semanas anteriores
ventas_anteriores = [125000, 98000, 147000, 132000, 110000]

# 1. Sumar todos los valores de la lista de ventas anteriores
total_ventas = sum(ventas_anteriores)

# 2. Contar la cantidad de registros o días evaluados
cantidad_semanas = len(ventas_anteriores)

# 3. Calcular el promedio matemático dividiendo el total entre la cantidad
promedio_ventas = total_ventas / cantidad_semanas

# 4. Encontrar la venta máxima y mínima del período anterior
venta_mayor = max(ventas_anteriores)
venta_menor = min(ventas_anteriores)

# Impresión en pantalla con formato limpio de dos decimales (.2f) y separadores de miles
print("=== REPORTE DE VENTAS ANTERIORES ===")
print(f"Total acumulado: ₡{total_ventas:,.2f}")
print(f"Promedio calculado: ₡{promedio_ventas:,.2f}")
print(f"Pico más alto: ₡{venta_mayor:,.2f}")
print(f"Pico más bajo: ₡{venta_menor:,.2f}")