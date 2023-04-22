gastos = []
descrs = []
ventas = []
prodts = []
names = []
charges = []
prod_chrgs = []
name_chrgs = []


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
    
    1) Ingresar gastos      3) ingresar ventas      5) Ingresar encargo     7) Mostar Balance
    2) Mostrar gastos       4) Motrar ventas        6) Mostrar encargo      8) Salir
    
    """)
    try:
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

        elif option == 7:
            print(f"Total de gastos: ${total}")
            print(f"Total en ventas: ${TotalSell}")
            balance = Balance(TotalSell, total)
            print(f"Balance: ${balance}")

        elif option == 5:
            charge = float(input("Ingresa el valor del encargo: "))
            prod_chrg = input("Ingresa el producto encargado: ")
            name_chrg = input("Ingresa el nombre del comprador: ")
            charges.insert(0, charge)
            prod_chrgs.insert(0, prod_chrg)
            name_chrgs.insert(0, name_chrg)

        elif option == 6:
            print(charges)
            print(prod_chrgs)
            print(name_chrgs)
            TotalCharges = ListSumation(charges)
            print(f"Total en encargos: $")


        elif option == 8:
            break

        else:
            print("No has ingresado la opcion correcta")


    except:
        print("Has ingresado un caracter invalido!")
