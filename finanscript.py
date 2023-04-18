
gastos = []
descrs = []

option=0

def ListSumation(a):
    if a == []:
       add = 0
    else:
       add = a[0] + ListSumation(a[1:])

    return add

while True:
    print("""
    1) ingresar gastos
    2) mostrar gastos 
    
    """)

    option = int(input("ingresa una opcion: "))



    if option == 1:
        gasto = float(input("ingresa el gasto: "))
        descr = input("Ingresa una descripcion: ")
        gastos.insert(0,gasto)
        descrs.insert(0,descr)

    elif option == 2:
        print(gastos)
        print(descrs)
        total = ListSumation(gastos)
        print(f"Total de gastos: {total}")

    else:
        print("No has ingresado la opcion correcta")