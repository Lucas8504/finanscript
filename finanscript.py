
gastos=[]

while True:
    print("""
    1) ingresar gastos
    2) mostrar gastos 
    
    """)

    opcion = int(input("ingresa una opcion: "))



    if opcion == 1:
        gasto = int(input("ingresa el gasto: "))
        gastos.insert(gasto)

    if opcion == 2:
        print(gastos)