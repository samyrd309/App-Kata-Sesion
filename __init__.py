import src.KataTeamProyect.main

program = src.KataTeamProyect.main

program.CreateRange(input())
program.CreateRange(input())
def seleccionarOpcion(opt):
    match opt:
        case 1:
            return program.integer_range_contains()
        case 2:
            return program.ContainsRange()
        case 3:
            return program.endPoints()
        case 4: 
            return program.Equals()
            
            