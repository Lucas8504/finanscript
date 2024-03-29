from typing import Union, Any
import tkinter as tk
from tkinter import filedialog
import openpyxl
from openpyxl.styles import PatternFill
from openpyxl.utils import get_column_letter


root = tk.Tk()
root.title("Excel con Tkinter")


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
def list_sumation(a):
    if not a:
        add = 0
    else:
        add = a[0] + list_sumation(a[1:])
    return add



# Metodo de balance
def Balance(a, b):
    balance = a - b
    return balance


# Metodo de suma en totales
def mas(a, b):
    add = a + b
    return add


# funcion de bolcado de datos a excel
def to_excel(data, c):
    for i in range(len(data)):
        worksheet.cell(row=i + 1, column=c, value=data[i])


# Funcion de volcado de datos a excel operacion
def to_excel_op(head, row1, data, row2, c):
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


# funcion de ancho de celdas
def adjust_column_width(worksheet):
    for column_cells in worksheet.columns:
        length = max(len(str(cell.value)) for cell in column_cells)
        worksheet.column_dimensions[get_column_letter(column_cells[0].column)].width = length + 1


while True:

    option = 0

    adjust_column_width(worksheet)  # Ajuste de columnas de acuerdo al contenido de las celdas
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
            to_excel(gastos, 1)
            to_excel(descrs, 2)
            background_color(worksheet, 2, gastos, 1, 3, 'E9C71B')  # Color de fondo de las celdas de excel
            background_color(worksheet, 1, 2, 1, 3, 'E9921B')

            wb.save('fpdsvasos.xlsx')  # guarda los datos a excel


        # Mostrar gastos
        elif option == 2:
            remove_str(gastos, "Gastos")
            remove_str(descrs, "Descripcion")
            print(gastos)
            print(descrs)
            total: float = list_sumation(gastos)
            print(f"Total de gastos: {total}")
            cel = 2
            cant = len(gastos) + 1
            to_excel_op("Gastos Totales", 1, f'=SUM(A{cel}:A{cant})', 2, 13)
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
            to_excel(ventas, 4)
            to_excel(prodts, 5)
            to_excel(names, 6)
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
            TotalSell = list_sumation(ventas)
            print(f"Total en ventas: ${TotalSell}")
            cel = 2
            cant = len(ventas) + 1
            to_excel_op("Ventas Totales", 1, f'=SUM(D{cel}:D{cant})', 2, 14)
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
                to_excel_op("Balance", 5, "=N2-M2", 6, 13)
                background_color(worksheet, 5, 7, 13, 14, '08CCDF')
                Totalspect = mas(balance, TotalCharges)
                print(f"Balance mas total de encargos: ${Totalspect}")
                to_excel_op("Balance mas total de encargos", 1, "=O2+M6", 2, 16)
                background_color(worksheet, 1, 3, 16, 17, '0891DF')
                wb.save('fpdsvasos.xlsx')

                input()
            except NameError:
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

            to_excel(charges, 9)
            to_excel(prod_chrgs, 10)
            to_excel(name_chrgs, 11)

            background_color(worksheet, 2, charges, 9, 12, 'BB09F9')
            background_color(worksheet, 1, 2, 9, 12, '9805CF')

            wb.save('fpdsvasos.xlsx')


        # Mostrar encargos
        elif option == 6:
            remove_str(charges, "Valor del encargo")
            remove_str(prod_chrgs, "Producto encargado")
            remove_str(name_chrgs, "Nombre del comprador")
            print(charges)
            print(prod_chrgs)
            print(name_chrgs)
            TotalCharges = list_sumation(charges)
            print(f"Total en encargos: ${TotalCharges}")

            cel = 2
            cant = len(charges) + 1
            to_excel_op("Total de encargos", 1, f'=SUM(I{cel}:I{cant})', 2, 15)

            background_color(worksheet, 1, 3, 15, 16, '9805CF')

            wb.save('fpdsvasos.xlsx')

            input()


        elif option == 8:  # Salir
            break

        else:
            print("No has ingresado la opcion correcta")
            input()


    except ValueError:
        print("Has ingresado un caracter invalido!")
        input()


root.mainloop()