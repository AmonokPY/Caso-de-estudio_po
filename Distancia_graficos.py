xf=[]
for i in range(9):
    eleccion=int(input("1 para normal 2 para lo otro: "))
    if eleccion==1:
        Vf = float(input("Ingrese la Vf: "))  # Convert input to float for calculations
        Vf = (Vf * 1000) / 3600  # Convert Vf from km/h to m/s (optional)
        
        Vo = float(input("Ingrese la Vo: "))  # Convert input to float
        Vo= (Vo * 1000) / 3600
        print("------------------")
        t = float(input("Ingrese la t: "))  # Convert input to float

        a = (Vf - Vo) / t  # Calculate acceleration

        x = Vo * t + 0.5 * a * (t**2)  # Use ** for exponentiation (t to the power of 2)
    else: 
        Vo = float(input("Ingrese la Vo: "))  # Convert input to float
        Vo= (Vo * 1000) / 3600
        print("------------------")
        t = float(input("Ingrese la t: "))  # Convert input to float
        x= Vo * t 
    xf.append(x)
    print(f"Vf = {Vf} m/s^2")
    print(f"Vo = {Vo} m/s^2")
    print(f"Aceleracion {Vf}-{Vo}/{t}= {a} m/s^2")  # Print acceleration with units
    print(f"Distancia {Vo}*{t}+ 1/2 *{a:.2f}*({t}^2) = {x} metros")   # Print distance with units
    print("----------------")
    print(f"suma total={sum(xf)}")