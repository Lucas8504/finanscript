
gastos=[]

option=0
while True:
    print("""
    1) ingresar gastos
    2) mostrar gastos 
    
    """)

    option = int(input("ingresa una opcion: "))



    if option == 1:
        gasto = int(input("ingresa el gasto: "))
        gasto.insert(gastos)

    elif option == 2:
        print(gastos)

    else:
        print("No has ingresado la opcion correcta")