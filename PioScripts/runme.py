import sys
import os
import pickle
from SolverConnection.solver import Solver
import subprocess
import time




# python runme.py C:/PioSOLVER/PioSOLVER2-pro.exe C:/PioSOLVER/PioSolverConnection-master/python_2_0/HU15bbsJT8.cfr
# python runme.py C:/PioSOLVER/PioSOLVER2-pro.exe C:/PioSOLVER/PioSolverConnection-master/python_2_0/HU8bbsQ85.cfr
# cd C:\PioSOLVER\PioSolverConnection-master\python_2_0
def main():
    #subprocess.run("cd C:\\PioSOLVER\\PioSolverConnection-master\\python_2_0 && python runme.py C:/PioSOLVER/PioSOLVER2-pro.exe C:/PioSOLVER/PioSolverConnection-master/python_2_0/HU15bbsJT8.cfr", shell=True)
    # Revisa si hay suficientes argumentos
    if len(sys.argv) <3:
        print("Needs 2 arguments (solver path and path to the .cfr file).")
        return

    # starts the solver process using the provided .exe path
    connection = Solver(solver=sys.argv[1])
    # report success
    print("Solver connected successfully")

    # now let's use created solver connection to call some commands
    # call and print the result of "show metadata" on the provided .cfr file
    metadata = connection.command(line =f"show_metadata {sys.argv[2]}")
    # print_lines(metadata)

    # load the tree
    output = connection.command(line=f"load_tree {sys.argv[2]}")
    print_lines(output)
    
    # clear = connection.command(line =f"reset_tree_info")
    # print_lines(clear)
    
    board = connection.command(line =f"set_board 2s2h8d")
    print_lines(board)
    # clearlines = connection.command(line =f"clear_lines")
    # print_lines(clearlines)    

    # addline = connection.command(line =f"add_line 30 30")
    # print_lines(addline)


    # buildtree = connection.command(line=f"build_tree")
    # print_lines(buildtree)

    # go = connection.command(line=f"go")
    # print_lines(go)

    # time.sleep(10)

    # stop = connection.command(line=f"stop")
    # print_lines(stop)

    # build = connection.command(line=f"show_tree_info")
    # print_lines(build)

    # show hands order (solver will return always the same answer)
    handorder = connection.command("show_hand_order")
    # print_lines(handorder)
    
    # show ranges
    print("Range OOP:")
    rangeOOP = connection.command("show_range OOP r")
    # print_lines(rangeOOP)



    #OOP



    #PRIMER NODO

    calcevOOPAI = connection.command("calc_ev_pp OOP r:0:b10")
    # print("EV OOP AI:")
    # print_lines(calcevOOPAI)

    calcevOOPX = connection.command("calc_ev_pp OOP r:0:c")
    # print("EV OOP fold:")
    # print_lines(calcevOOPX)

    #TRAS FLOP X PROPIO Y BET 10 RIVAL

    calcevOOPB10AI = connection.command("calc_ev_pp OOP r:0:c:b10:b80")
    # print("EV OOP AI:")
    # print_lines(calcevOOPB10AI)

    calcevOOPB10F = connection.command("calc_ev_pp OOP r:0:c:b10:f")
    # print("EV OOP fold:")
    # print_lines(calcevOOPB10F)


    calcevOOPB80AI = connection.command("calc_ev_pp OOP r:0:c:b80:c")


    #IP

    #vs X rival
    calcevIPcb80 = connection.command("calc_ev_pp IP r:0:c:b80")
    # print("EV IP:")
    # print_lines(calcevIPcb80)

    calcevIPcc = connection.command("calc_ev_pp IP r:0:c:c")
    # print("EV IP:")
    # print_lines(calcevIPcc)

    #vs b80 rival

    calcevIPb80c = connection.command("calc_ev_pp IP r:0:c:b80:c")
    # print("EV IP:")
    # print_lines(calcevIPb80c)

    calcevIPb80f = connection.command("calc_ev_pp IP r:0:c:b80:f")
    # print("EV IP:")
    # print_lines(calcevIPb80f)


    #vs b10 rival

    calcevIPb10c = connection.command("calc_ev_pp IP r:0:c:b10:c")
    # print("EV IP:")
    # print_lines(calcevIPb10c)

    calcevIPb10f = connection.command("calc_ev_pp IP r:0:c:b10:f")
    # print("EV IP:")
    # print_lines(calcevIPb10f)

    calcevIPb10AI = connection.command("calc_ev_pp IP r:0:c:b10:b80")
    # print("EV IP:")
    # print_lines(calcevIPb10AI)


    calcevIP = connection.command("calc_ev_pp IP r:0")
    # print("EV IP:")
    # print_lines(calcevIP)

    # calcevIPP = connection.command("calc_ev IP r")
    # print("EV IP:")
    # print_lines(calcevIPP)


    #showalllines
    # calc_eq_preflop = connection.command("calc_eq_preflop IP")
    # print("calc_eq_preflop:")
    # print_lines(calc_eq_preflop)


    # calc_results = connection.command("calc_results")
    # print("calc_results:")
    # print_lines(calc_results)
    

    show_all_lines= connection.command("show_all_lines")
    # print("all lines:")
    # print_lines(show_all_lines)

#OOP FILES


     # Open a file for writing
    with open('calcevOOPAI.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPAI))
        # Open a file for writing
    with open('calcevOOPX.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPX))

   
    with open('calcevOOPB10AI.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPB10AI))
        # Open a file for writing

    with open('calcevOOPB10F.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPB10F))
        # Open a file for writing

    with open('calcevOOPB80AI.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPB80AI))

#IP FILES


    with open('calcevIPcb80.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPcb80))
        # Open a file for writing

    with open('calcevIPcc.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPcc))

    with open('calcevIPb80c.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPb80c))

    with open('calcevIPb10c.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPb10c))
    with open('calcevIPb10AI.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPb10AI))

    





    # we have to explicitely close the solver process
    print("Closing connection:")
    connection.exit()
    print("Connection closed.")
    print('Done.')

def print_lines(lines):
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()