

# listas que guardan informcion ingresada por usuario
gastos = []
descrs = []
ventas = []
prodts = []
names = []
charges = []
prod_chrgs = []
name_chrgs = []


option = 0

# Metodo para suma del contenido de las listas
def ListSumation(a):
    if a == []:
        add = 0
    else:
        add = a[0] + ListSumation(a[1:])
    return add

# Metodo de balance
def Balance(a,b):
    balance = a - b
    return balance

# Metodo de suma en totales
def Mas(a, b):
    add = a + b
    return add


while True:
    print(""" 
    
    Elija una opcion
    
    1) Ingresar gastos      3) ingresar ventas      5) Ingresar encargo     7) Mostar Balance
    2) Mostrar gastos       4) Motrar ventas        6) Mostrar encargo      8) Salir
    
    """)
    try:         # manejo de error en caracteres invalidos
        option = int(input("""ingresa una opcion: 
        """))

        if option == 1:         # ingresar gastos
            gasto = float(input("ingresa el gasto: "))
            descr = input("Ingresa una descripcion: ")
            gastos.insert(0, gasto)
            descrs.insert(0, descr)

        elif option == 2:       # Mostrar gastos
            print(gastos)
            print(descrs)
            total = ListSumation(gastos)
            print(f"Total de gastos: {total}")
            input()

        elif option == 3:       # Ingresar ventas
            venta = float(input("Ingresa el valor de la venta: "))
            prod = input("Ingresa el producto vendido: ")
            name = input("Ingresa el nombre del comprador: ")
            ventas.insert(0, venta)
            prodts.insert(0, prod)
            names.insert(0, name)

        elif option == 4:       # Mostrar ventas
            print(ventas)
            print(prodts)
            print(names)
            TotalSell = ListSumation(ventas)
            print(f"Total en ventas: ${TotalSell}")
            input()

        elif option == 7:        # Mostrar balance
            try:        # Manejo de error por listas vacias

                print(f"Total de gastos: ${total}")
                print(f"Total en ventas: ${TotalSell}")
                print(f"Total en encargos: ${TotalCharges}")
                balance = Balance(TotalSell, total)
                print(f"Balance: ${balance}")
                Totalspect = Mas(balance, TotalCharges)
                print(f"Balance mas total de encargos: ${Totalspect}")
                input()
            except:
                print("No hay datos para un balance")
                input()

        elif option == 5:          # Ingresar encargos
            charge = float(input("Ingresa el valor del encargo: "))
            prod_chrg = input("Ingresa el producto encargado: ")
            name_chrg = input("Ingresa el nombre del comprador: ")
            charges.insert(0, charge)
            prod_chrgs.insert(0, prod_chrg)
            name_chrgs.insert(0, name_chrg)

        elif option == 6:           # Mostrar encargos
            print(charges)
            print(prod_chrgs)
            print(name_chrgs)
            TotalCharges = ListSumation(charges)
            print(f"Total en encargos: ${TotalCharges}")
            input()


        elif option == 8:           # Salir
            break

        else:
            print("No has ingresado la opcion correcta")
            input()


    except:
        print("Has ingresado un caracter invalido!")
        input()
