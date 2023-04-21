gastos = []
descrs = []
ventas = []
prodts = []
names = []

option = 0


def ListSumation(a):
    if a == []:
        add = 0
    else:
        add = a[0] + ListSumation(a[1:])

    return add

def Balance(a,b):
    balance = a - b
    return balance



while True:
    print(""" 
    Elija una opcion
    
    1) Ingresar gastos      4) Mostrar ventas
    2) Mostrar gastos       5) Mostrar balance
    3) Ingresar ventas      6) Salir
    
    """)

    option = int(input("ingresa una opcion: "))

    if option == 1:
        gasto = float(input("ingresa el gasto: "))
        descr = input("Ingresa una descripcion: ")
        gastos.insert(0, gasto)
        descrs.insert(0, descr)

    elif option == 2:
        print(gastos)
        print(descrs)
        total = ListSumation(gastos)
        print(f"Total de gastos: {total}")

    elif option == 3:
        venta = float(input("Ingresa el valor de la venta: "))
        prod = input("Ingresa el producto vendido: ")
        name = input("Ingresa el nombre del comprador: ")
        ventas.insert(0, venta)
        prodts.insert(0, prod)
        names.insert(0, name)

    elif option == 4:
        print(ventas)
        print(prodts)
        print(names)
        TotalSell = ListSumation(ventas)
        print(f"Total en ventas: ${TotalSell}")

    elif option == 5:
        print(f"Total de gastos: ${total}")
        print(f"Total en ventas: ${TotalSell}")
        balance = Balance(TotalSell, total)
        print(f"Balance: ${balance}")

    elif option == 6:
        break

    else:
        print("No has ingresado la opcion correcta")
