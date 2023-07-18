import sys
import os
import pickle
from SolverConnection.solver import Solver
import subprocess
import time

from searchturn import contenidoTurn_final

class River:
    from CardDetectorRiver import contenidoRiver
    time.sleep(2)
    river=contenidoRiver
# python runmeRiver.py C:/PioSOLVER/PioSOLVER2-pro.exe C:/PioSOLVER/PioSolverConnection-master/python_2_0/HU15bbsJT8.cfr
# python runmeRiver.py C:/PioSOLVER/PioSOLVER2-pro.exe C:/PioSOLVER/PioSolverConnection-master/python_2_0/HU8bbsQ85.cfr
# cd C:\PioSOLVER\PioSolverConnection-master\python_2_0
def main():

    #subprocess.run("cd C:\\PioSOLVER\\PioSolverConnection-master\\python_2_0 && python runme.py C:/PioSOLVER/PioSOLVER2-pro.exe C:/PioSOLVER/PioSolverConnection-master/python_2_0/HU15bbsJT8.cfr", shell=True)

    # check if there are enough command line arguments provided
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
    
    
    # clearlines = connection.command(line =f"clear_lines")
    # print_lines(clearlines)    

    # board = connection.command(line =f"set_board AsKhJd")
    # print_lines(board)

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


    print("Range IP:")
    rangeIP = connection.command("show_range IP r")
    # print_lines(rangeIP)
    # calculate EV

    #PRIMER NODO TRAS TURN

    calcevOOPAIRiver = connection.command("calc_ev_pp OOP r:0:c:c:"+contenidoTurn_final+":c:c:"+River.river+"b80")
    print("EV OOP AI:")
    print_lines(calcevOOPAIRiver)

    calcevOOPXRiver = connection.command("calc_ev_pp OOP r:0:c:c:"+contenidoTurn_final+":c:c:"+River.river+"c")
    print("EV OOP fold:")
    print_lines(calcevOOPXRiver)

    #TRAS River X PROPIO Y BET 10 RIVAL

    calcevOOPB10AIVSB10RIVAI = connection.command("calc_ev_pp OOP r:0:c:c:"+contenidoTurn_final+":c:c:"+River.river+"c:b10:b80")
    print("EV OOP AI:")
    print_lines(calcevOOPB10AIVSB10RIVAI)

    calcevOOPB10FVSB10RIVCALL = connection.command("calc_ev_pp OOP r:0:c:c:"+contenidoTurn_final+":c:c:"+River.river+"c:b10:c")
    print("EV OOP fold:")
    print_lines(calcevOOPB10FVSB10RIVCALL)


    #TRAS TURN X PROPIO Y BET 80 RIVAL

    calcevOOPB10AIVSB80RIVAICALL = connection.command("calc_ev_pp OOP r:0:c:c:"+contenidoTurn_final+":c:c:"+River.river+"c:b80:c")
    print("EV OOP AI:")
    print_lines(calcevOOPB10AIVSB80RIVAICALL)


    #IP

    #vs X rival en flop y X turn
    calcevIPcb80RIV = connection.command("calc_ev_pp IP r:0:c:c:"+contenidoTurn_final+":c:c:"+River.river+"c:b80")
    print("EV IP:")
    print_lines(calcevIPcb80RIV)

    calcevIPccRIV = connection.command("calc_ev_pp IP r:0:c:c:"+contenidoTurn_final+":c:c:"+River.river+"c:c")
    print("EV IP:")
    print_lines(calcevIPccRIV)

    #vs b10 rival en flop y X turn
    calcevIPcb80Fb10RIV = connection.command("calc_ev_pp IP r:0:c:c:"+contenidoTurn_final+":c:c:"+River.river+"b80:c")
    print("EV IP:")
    print_lines(calcevIPcb80Fb10RIV)

    calcevIPccFb10RIV = connection.command("calc_ev_pp IP r:0:b10:c:"+contenidoTurn_final+":c:c:"+River.river+"c:c")
    print("EV IP:")
    print_lines(calcevIPccFb10RIV)


    calcevIPb80cXF = connection.command("calc_ev_pp IP r:0:b10:c:"+contenidoTurn_final+":c:c:"+River.river+"c:b80")
    print("EV IP:")
    print_lines(calcevIPb80cXF)


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
    print("all lines:")
    # print_lines(show_all_lines)


      #OOP FILES


     # Open a file for writing
    with open('calcevOOPAIRiver.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPAIRiver))
        # Open a file for writing
    with open('calcevOOPXRiver.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPXRiver))

   
    with open('calcevOOPB10AIVSB10RIVAI.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPB10AIVSB10RIVAI))
        # Open a file for writing

    with open('calcevOOPB10FVSB10RIVCALL.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPB10FVSB10RIVCALL))
        # Open a file for writing

    with open('calcevOOPB10AIVSB80RIVAICALL.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPB10AIVSB80RIVAICALL))
        # Open a file for writing

#IP FILES


    with open('calcevIPcb80RIV.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPcb80RIV))
        # Open a file for writing

    with open('calcevIPccRIV.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPccRIV))

    with open('calcevIPcb80Fb10RIV.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPcb80Fb10RIV))

    with open('calcevIPccFb10RIV.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPccFb10RIV))

    with open('calcevIPb80cXF.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPb80cXF))

    with open('calcevIPb80cXF.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPb80cXF))


   
   
    # we have to explicitely close the solver process
    print("Closing connection:")
    connection.exit()
    print("Connection closed.")
    print('Done.')
    print(contenidoTurn_final)

def print_lines(lines):
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()