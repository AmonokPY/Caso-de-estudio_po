import math

def vector_xy(nom, uni, grado, direccion):
    uni = int(uni)
    grado = int(grado)
    direccion = direccion.upper()
    grado_rad = math.radians(grado)  # Convertir grados a radianes
    vx = uni * math.cos(grado_rad)
    vy = uni * math.sin(grado_rad)
    
    if direccion == "NO":
        vx = -abs(vx)
        vy = abs(vy)
    elif direccion == "SO":
        vx = -abs(vx)
        vy = -abs(vy)
    elif direccion == "SE" or direccion == "SUR":
        vx = abs(vx)
        vy = -abs(vy)
    elif direccion == "NE":
        vx = abs(vx)
        vy = abs(vy)  # Corregido para que sea vy
    
    print(f"{nom}x = {uni} * cos({grado}) = {vx}")
    print(f"{nom}y = {uni} * sin({grado}) = {vy}")
    return vx, vy

# Entrada de los vectores
uniA, gradoA, direccionA = input("Ingrese el vector A (uniA, gradoA, direccionA): ").split(",")
ax, ay = vector_xy("A", uniA, gradoA, direccionA)

uniB, gradoB, direccionB = input("Ingrese el vector B (uniB, gradoB, direccionB): ").split(",")
bx, by = vector_xy("B", uniB, gradoB, direccionB)

uniC, gradoC, direccionC = input("Ingrese el vector C (uniC, gradoC, direccionC): ").split(",")
cx, cy = vector_xy("C", uniC, gradoC, direccionC)

# Cálculo de la resultante
print("-------Resultante------")

suma_y = ay + by + cy
print(f"La suma de y {ay} + {by} +{ cy} = {suma_y}")

suma_x = ax + bx + cx
print(f"La suma de x {ax} + {bx} +{ cx} = {suma_x}")

# Magnitud de la resultante
runi = math.sqrt(suma_x**2 + suma_y**2)
print(f"Unidades de la resultante ({suma_x**2})({suma_y**2}) = {runi}")

# Ángulo de la resultante en grados
rgrados = math.degrees(math.atan2(suma_y, suma_x))
print(f"Grados de la resultante {suma_y}/{suma_x} = {rgrados}")
