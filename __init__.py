
import src.main

program = src.main




def seleccionarOpcion(opt):
    if opt == 1:
        defaultRange =  program.CreateRange(input("Ingrese el rango por default: "))
        InputRange =  program.CreateRange(input("Ingrese los valores a identificar: "))
        return program.integer_range_contains(defaultRange, InputRange)
    elif opt == 2:
        defaultRange =  program.CreateRange(input("Ingrese el rango por default: "))
        InputRange =  program.CreateRange(input("Ingrese los valores a identificar: "))
        return program.ContainsRange(defaultRange, InputRange)
    elif opt == 3:
        InputRange =  program.CreateRange(input("Ingrese los valores a identificar los endpoints: "))
        return program.endPoints(InputRange)
    elif opt == 4:
        arr1 =  program.CreateRange(input("Ingrese el primer valor: "))
        arr2 =  program.CreateRange(input("Ingrese el segundo valor: "))
        return program.Equals()
    elif opt == 5:
        InputRange =  program.CreateRange(input("Ingrese el rango: "))
        return program.getAllPoint()
    else:
        return "Opcion invalida"

optcontinuar = 's'
while optcontinuar.lower() == 's' :
    val = input("Ingrese la opcion que desea consultar \n1.Integer Range Contains \n2. Contains Range \n3. EndPoints \n4. Equals\n Ingrese la opción: ")
    print(seleccionarOpcion(int(val)))
    optcontinuar = input("¿Desea contuniar usando el programa s - n?")
