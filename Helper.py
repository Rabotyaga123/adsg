#file_python = open("AAAAA.py", "w")while end <= 4:
from Convert_to_AIG import generate_AIG
import os
import aiger
end = 0
while end <= 1000:
    file_python = open("Convert_to_AIG.py", "w")
    file_python.write("import aiger\n\n")
    file_python.write("def generate_AIG(end):\n")
    file_python.write("     X0, X1, X2, X3 = aiger.atoms('X0', 'X1', 'X2', 'X3')\n")
    file_python.write("     X4, X5, X6, X7 = aiger.atoms('X4', 'X5', 'X6', 'X7')\n")
    file_python.write("     X8, X9, X10, X11 = aiger.atoms('X8', 'X9', 'X10', 'X11')\n")
    file_python.write("     X12, X13, X14, X15 = aiger.atoms('X12', 'X13', 'X14', 'X15')\n")
    file_python.write("     X16, X17, X18, X19 = aiger.atoms('X16', 'X17', 'X18', 'X19')\n\n")
    file_python.close
    file_function = open("{}F.txt".format(end), "r")
    function = file_function.readlines()
    file_function.close
    file_python = open("Convert_to_AIG.py", "a")
    file_python.write("     ")
    for i in function:
        file_python.write(i)
    file_python.write("\n")
    file_python.write("     print(f.aig)\n")
    file_python.write("     file_convert = open(" + '"' + '{' + '}' + 'D' + '.aag' + '"' + '.format(end)' + ',' + "'" + 'w' + "'"")\n")
    file_python.write("     file_convert.write(" +"'"+ '{'+'}'+"'"+'.format(f.aig)'+ ')')
    file_python.close
    # print(end)
    # print(i)
    
    generate_AIG(end)
    end += 1