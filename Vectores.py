import math
def vector_xy(nom,uni,grado,direccion):
    uni=int(uni)
    grado=int(grado)
    direccion=direccion.upper()
    vx=uni*math.cos(grado)
    vy=uni*math.sin(grado)
    if direccion=="NO" :
        vx=-abs(vx)
        vy=abs(vy)
    elif direccion=="SO":
        vx=-abs(vx)
        vy=-abs(vy)
    elif direccion=="SE"or direccion=="SUR":
        vx=abs(vx)
        vy=-abs(vy)
    elif direccion=="NE":
        vx=abs(vx)
        vy=abs(vy)
    print(f"{nom}x = {uni}*cos({grado}) = {vx}")
    print(f"{nom}y = {uni}*sin({grado}) = {vy}")
    return vx,vy

# nom=input("Ingrese el nombre del vector; ")
a=uniA,gradoA,direccionA=input(f"ingrese el vector A; ").split(",")
ax,ay=vector_xy("A",uniA,gradoA,direccionA)
b=uniB,gradoB,direccionB=input(f"ingrese el vector B; ").split(",")
bx,by=vector_xy("B",uniB,gradoB,direccionB)
c=uniC,gradoC,direccionC=input(f"ingrese el vector C; ").split(",")
cx,cy=vector_xy("C",uniC,gradoC,direccionC)
print("-------resultante------")
suma_x= ax + bx + cx
print(f"la suma de x = {suma_x}")
suma_y= ay + by + cy
print(f"la suma de y = {suma_y}")
runi=math.sqrt((suma_x)**2+(suma_y)**2)
print(f"unidades del resultante= {runi}")
rgrados = math.degrees(math.atan2(suma_y, suma_x))
print(f"Grados de la resultante:{rgrados}")

