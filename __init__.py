from  src.KataTeamProyect import main

program = main




def seleccionarOpcion(opt):
    match opt:
        case 1:
            defaultRange =  program.CreateRange(input())
            InputRange =  program.CreateRange(input())
            return program.integer_range_contains(defaultRange, InputRange)
        case 2:
            defaultRange =  program.CreateRange(input())
            InputRange =  program.CreateRange(input())
            return program.ContainsRange(defaultRange, InputRange)
        case 3:
            InputRange =  program.CreateRange(input())
            return program.endPoints(InputRange)
        case 4: 
            defaultRange =  program.CreateRange(input())
            InputRange =  program.CreateRange(input())
            return program.Equals()
            
def __init__ ():
    return

print(seleccionarOpcion(input("Ingrese la opcion que desea consultar \n1.Integer Range Contains \n2. Contains Range \n3. EndPoints \n Equals ")))