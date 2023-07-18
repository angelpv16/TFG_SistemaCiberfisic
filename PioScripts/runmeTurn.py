import sys
import os
import pickle
from SolverConnection.solver import Solver
import subprocess
import time


class Turn:
    from CardDetectorTurn import contenidoTurn
    time.sleep(2)
    turn=contenidoTurn
    



# python runme.py C:/PioSOLVER/PioSOLVER2-pro.exe C:/PioSOLVER/PioSolverConnection-master/python_2_0/HU15bbsJT8.cfr
# python runme.py C:/PioSOLVER/PioSOLVER2-pro.exe C:/PioSOLVER/PioSolverConnection-master/python_2_0/HU8bbsQ85.cfr
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

    calcevOOPAITurn = connection.command("calc_ev_pp OOP r:0:c:c:"+Turn.turn+":b80")
    print("EV OOP AI:")
    print_lines(calcevOOPAITurn)

    calcevOOPXTurn = connection.command("calc_ev_pp OOP r:0:c:c:"+Turn.turn+":c")
    print("EV OOP fold:")
    print_lines(calcevOOPXTurn)

    #TRAS TURN X PROPIO Y BET 10 RIVAL

    calcevOOPB10AIVSB10 = connection.command("calc_ev_pp OOP r:0:c:c:"+Turn.turn+":c:b10:b80")
    print("EV OOP AI:")
    print_lines(calcevOOPB10AIVSB10)

    calcevOOPB10FVSB10 = connection.command("calc_ev_pp OOP r:0:c:c:"+Turn.turn+":c:b10:f")
    print("EV OOP fold:")
    print_lines(calcevOOPB10FVSB10)


    #TRAS TURN X PROPIO Y BET 80 RIVAL

    calcevOOPB10AIVSB80 = connection.command("calc_ev_pp OOP r:0:c:c:"+Turn.turn+":c:b80:c")
    print("EV OOP AI:")
    print_lines(calcevOOPB10AIVSB80)


    #IP

    #vs X rival en flop y X turn
    calcevIPcb80 = connection.command("calc_ev_pp IP r:0:c:c:"+Turn.turn+":c:b80")
    print("EV IP:")
    print_lines(calcevIPcb80)

    calcevIPcc = connection.command("calc_ev_pp IP r:0:c:c:"+Turn.turn+":c:c")
    print("EV IP:")
    print_lines(calcevIPcc)

    #vs b10 rival en flop y X turn
    calcevIPcb80Fb10 = connection.command("calc_ev_pp IP r:0:b10:c:"+Turn.turn+":c:b80")
    print("EV IP:")
    print_lines(calcevIPcb80Fb10)

    calcevIPccFb10 = connection.command("calc_ev_pp IP r:0:b10:c:"+Turn.turn+":c:c")
    print("EV IP:")
    print_lines(calcevIPccFb10)


    #vs b80 rival EN X FLOP

    calcevIPb80cXF = connection.command("calc_ev_pp IP r:0:c:c:"+Turn.turn+":b80:c")
    print("EV IP:")
    print_lines(calcevIPb80cXF)

    calcevIPb80fXF = connection.command("calc_ev_pp IP r:0:c:c:"+Turn.turn+":b80:f")
    print("EV IP:")
    print_lines(calcevIPb80fXF)

    #vs b80 rival EN B10 FLOP

    calcevIPb80cBF = connection.command("calc_ev_pp IP r:0:b10:c:"+Turn.turn+":b80:c")
    print("EV IP:")
    print_lines(calcevIPb80cBF)

    calcevIPb80fBF = connection.command("calc_ev_pp IP r:0:b10:c:"+Turn.turn+":b80:f")
    print("EV IP:")
    print_lines(calcevIPb80fBF)
    

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
    with open('calcevOOPAITurn.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPAITurn))
        # Open a file for writing
    with open('calcevOOPXTurn.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPXTurn))

   
    with open('calcevOOPB10AIVSB10.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPB10AIVSB10))
        # Open a file for writing

    with open('calcevOOPB10FVSB10.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPB10FVSB10))
        # Open a file for writing

    with open('calcevOOPB10AIVSB80.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevOOPB10AIVSB80))
        # Open a file for writing

#IP FILES


    with open('calcevIPcb80.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPcb80))
        # Open a file for writing

    with open('calcevIPcc.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPcc))

    with open('calcevIPcb80Fb10.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPcb80Fb10))

    with open('calcevIPccFb10.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPccFb10))

    with open('calcevIPb80cXF.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPb80cXF))

    with open('calcevIPb80fXF.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPb80fXF))

    with open('calcevIPb80cBF.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPb80cBF))

    with open('calcevIPb80fBF.txt', 'w') as f:
    # Write the value of the variable to the file
        f.write(str(calcevIPb80fBF))

    # Calculate the strategy for the OOP player at the root node
    # strategy = connection.command("show_range OOP r:b30:c")

    # print("strategy:")
    # # Print the strategy
    # print_lines(strategy)
    # print_lines(board)
   
    # we have to explicitely close the solver process
    print("Closing connection:")
    connection.exit()
    print("Connection closed.")
    print('Done.')
    print(Turn.turn)

def print_lines(lines):
    for line in lines:
        print(line)

if __name__ == "__main__":
    main()