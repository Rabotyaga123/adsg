import aiger

def generate_AIG(end):
     X0, X1, X2, X3 = aiger.atoms('X0', 'X1', 'X2', 'X3')
     X4, X5, X6, X7 = aiger.atoms('X4', 'X5', 'X6', 'X7')
     X8, X9, X10, X11 = aiger.atoms('X8', 'X9', 'X10', 'X11')
     X12, X13, X14, X15 = aiger.atoms('X12', 'X13', 'X14', 'X15')
     X16, X17, X18, X19 = aiger.atoms('X16', 'X17', 'X18', 'X19')

     f = (X0|X1)&(~X0&X1)|(X0&~X1)|(X0&X1)
     print(f.aig)
     file_convert = open("{}D.aag".format(end),'w')
     file_convert.write('{}'.format(f.aig))