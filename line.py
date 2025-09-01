def line():
    A = float(input("Ingrese el coeficiente A: "))
    B = float(input("Ingrese el coeficiente B: "))
    X1 = float(input("Ingrese el coeficiente X1: "))
    X2 = float(input("Ingrese el coeficiente X2: "))
    print(f"""El coeficiente A de su ecuación de la recta es: {A}
El coeficiente B de su ecuación de la recta es: {B}
El coeficiente X1 de su ecuación de la recta es: {X1}
El coeficiente X2 de su ecuación de la recta es: {X2}""")

    print(f"\nPara la siguiente ecuación:\n\tY = {A}X + {B}")
    Y1 = (A*X1 + B)
    Y2 = (A*X2 + B)
    P1 = (X1, Y1)
    P2 = (X2, Y2)

    print(f"\nDados los siguientes puntos:\n\tP1 {P1}\n\tP2 {P2}")
    
    dist = ((X2 - X1)**2 + (Y2 - Y1)**2)**(1/2)
    print(f"\nLa distancia entre ellos es: {dist}")
    #print("TO DO")