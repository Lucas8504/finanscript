from typing import Union, Any

import openpyxl
from openpyxl.styles import PatternFill
from openpyxl.utils import get_column_letter


# Excel
wb = openpyxl.Workbook()

worksheet = wb.active

# listas que guardan informcion ingresada por usuario
gastos = []
descrs = []
ventas = []
prodts = []
names = []
charges = []
prod_chrgs = []
name_chrgs = []


fill_pattern = PatternFill(patternType='solid', fgColor='C64747')


# Metodo para suma del contenido de las listas
def ListSumation(a):
    if not a:
        add = 0
    else:
        add = a[0] + ListSumation(a[1:])
    return add


# Metodo de balance
def Balance(a, b):
    balance = a - b
    return balance


# Metodo de suma en totales
def Mas(a, b):
    add = a + b
    return add


# funcion de bolcado de datos a excel
def ToExcel(data, c):
    for i in range(len(data)):
        worksheet.cell(row=i + 1, column=c, value=data[i])


# Funcion de volcado de datos a excel operacion
def ToExcel_Op(head, row1, data, row2, c):
    worksheet.cell(row=row1, column=c, value=head)
    worksheet.cell(row=row2, column=c, value=data)


# Funcion de encabezado
def header(list, valor):
    if valor in list:
        list.remove(valor)
    list.insert(0, valor)
    return list


# Funcion removedora de encabezados
def remove_str(list, data):
    if data in list:
        list.remove(data)
    return list

# Funcion de color de fondo de celdas de excel
def background_color(worksheet, start_row, end_row, c1, c2, color):
    fill = PatternFill(start_color=color, end_color=color, fill_type='solid')
    if isinstance(end_row, list):
        end = len(end_row) + 1
    else:
        end = end_row

    for row in range(start_row, end):
        for col in range(c1, c2):
            col_letter = get_column_letter(col)
            cell = worksheet['{}{}'.format(col_letter, row)]
            cell.fill = fill


while True:

    option = 0

    print(""" 
    
    Elija una opcion
    
    1) Ingresar gastos      3) ingresar ventas      5) Ingresar encargo     7) Mostar Balance
    2) Mostrar gastos       4) Motrar ventas        6) Mostrar encargo      8) Salir
    
    """)
    try:  # manejo de error en caracteres invalidos
        option = int(input("""ingresa una opcion: """))

        # Ingresar Gastos
        if option == 1:
            gasto = float(input("ingresa el gasto: "))
            descr = input("Ingresa una descripcion: ")
            gastos.insert(0, gasto)
            header(gastos, "Gastos")
            descrs.insert(0, descr)
            header(descrs, "Descripcion")
            ToExcel(gastos, 1)
            ToExcel(descrs, 2)
            background_color(worksheet, 2, gastos, 1, 3, 'E9C71B')  # Color de fondo de las celdas de excel
            background_color(worksheet, 1, 2, 1, 3, 'E9921B')

            wb.save('fpdsvasos.xlsx')                     # guarda los datos a excel


        # Mostrar gastos
        elif option == 2:
            remove_str(gastos, "Gastos")
            remove_str(descrs, "Descripcion")
            print(gastos)
            print(descrs)
            total: Union[float, Any] = ListSumation(gastos)
            print(f"Total de gastos: {total}")
            cel = 2
            cant = len(gastos) + 1
            ToExcel_Op("Gastos Totales", 1, f'=SUM(A{cel}:A{cant})', 2, 13)
            background_color(worksheet, 1, 3, 13, 14, 'E9921B')

            wb.save('fpdsvasos.xlsx')

            input()


        # Ingresar ventas
        elif option == 3:
            venta = float(input("Ingresa el valor de la venta: "))
            prod = input("Ingresa el producto vendido: ")
            name = input("Ingresa el nombre del comprador: ")
            ventas.insert(0, venta)
            header(ventas, "Ventas")
            prodts.insert(0, prod)
            header(prodts, "Productos")
            names.insert(0, name)
            header(names, "Nombre del comprador")
            ToExcel(ventas, 4)
            ToExcel(prodts, 5)
            ToExcel(names, 6)
            background_color(worksheet, 2, ventas, 4, 7, '58DB4B')
            background_color(worksheet, 1, 2, 4, 7, '1CBD0C')

            wb.save('fpdsvasos.xlsx')


        # Mostrar ventas
        elif option == 4:
            remove_str(ventas, "Ventas")
            remove_str(prodts, "Productos")
            remove_str(names, "Nombre del comprador")
            print(ventas)
            print(prodts)
            print(names)
            TotalSell = ListSumation(ventas)
            print(f"Total en ventas: ${TotalSell}")
            cel = 2
            cant = len(ventas) + 1
            ToExcel_Op("Ventas Totales", 1, f'=SUM(D{cel}:D{cant})', 2, 14)
            background_color(worksheet, 1, 3, 14, 15, '1CBD0C')

            wb.save('fpdsvasos.xlsx')

            input()


        # Mostrar balance
        elif option == 7:
            try:  # Manejo de error por listas vacias

                print(f"Total de gastos: ${total}")
                print(f"Total en ventas: ${TotalSell}")
                print(f"Total en encargos: ${TotalCharges}")
                balance = Balance(TotalSell, total)
                print(f"Balance: ${balance}")
                ToExcel_Op("Balance", 5, "=N2-M2", 6, 13)
                Totalspect = Mas(balance, TotalCharges)
                print(f"Balance mas total de encargos: ${Totalspect}")
                ToExcel_Op("Balance mas total de encargos", 5, "=O2+M6", 6, 15)

                wb.save('fpdsvasos.xlsx')
                input()
            except:
                print("No hay datos para un balance")
                input()


        # Ingresar encargos
        elif option == 5:
            charge = float(input("Ingresa el valor del encargo: "))
            prod_chrg = input("Ingresa el producto encargado: ")
            name_chrg = input("Ingresa el nombre del comprador: ")
            charges.insert(0, charge)
            header(charges, "Valor del encargo")
            prod_chrgs.insert(0, prod_chrg)
            header(prod_chrgs, "Producto encargado")
            name_chrgs.insert(0, name_chrg)
            header(name_chrgs, "Nombre del comprador")

            ToExcel(charges, 9)
            ToExcel(prod_chrgs, 10)
            ToExcel(name_chrgs, 11)

            wb.save('fpdsvasos.xlsx')


        # Mostrar encargos
        elif option == 6:
            remove_str(charges, "Valor del encargo")
            remove_str(prod_chrgs, "Producto encargado")
            remove_str(name_chrgs, "Nombre del comprador")
            print(charges)
            print(prod_chrgs)
            print(name_chrgs)
            TotalCharges = ListSumation(charges)
            print(f"Total en encargos: ${TotalCharges}")

            cel = 2
            cant = len(charges) + 1
            ToExcel_Op("Total de encargos", 1, f'=SUM(I{cel}:I{cant})', 2, 15)

            wb.save('fpdsvasos.xlsx')

            input()


        elif option == 8:  # Salir
            break

        else:
            print("No has ingresado la opcion correcta")
            input()


    except:
        print("Has ingresado un caracter invalido!")
        input()