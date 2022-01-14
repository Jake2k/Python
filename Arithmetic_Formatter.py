import operator

def arithmetic_arranger(lista,answers):
    error_checking(lista)
    top_number = []
    bottom_number = []
    lines = []
    answer_list = []
    for equation in lista:
        listb = equation.split(" ")
        error_checking2(listb[0],listb[2])
        top_number.append(listb[0])
        symbol_number = listb[1] + " " + listb[2]
        bottom_number.append(symbol_number)
        line_len = lines_func(listb[0], symbol_number)
        lines.append("-" * line_len)
        op_func = set_symbol(listb[1])
        if "-" not in listb[1]:
            if "+" not in listb[1]:
                raise Exception("Operator must be + or -")
        answer = op_func(int(listb[0]),int(listb[2]))
        answer_list.append(answer)
        
    print ("{:>8}{:>8}{:>8}{:>8}".format(*top_number))
    print ("{:>8}{:>8}{:>8}{:>8}".format(*bottom_number))
    print ("{:>8}{:>8}{:>8}{:>8}".format(*lines))
    if answers == True:
        print ("{:>8}{:>8}{:>8}{:>8}".format(*answer_list))
    
def set_symbol(symbol):
    op_func = ops[symbol]
    return op_func        

def lines_func(top_number,symbol_number):
    if len(symbol_number) >= len(top_number[0]):
        line_len = len(symbol_number)
    else:
        line_len = len(top_number[0])
    return line_len

def error_checking(lista):
    if len(lista) > 4:
        raise ValueError("Too many problems supplied")

def error_checking2(listb0,listb2):
    if listb0.isdigit() == False or listb2.isdigit() == False:
        raise Exception("Error: Numbers must only contain digits")
    if len(listb0) > 4 or len(listb2) > 4:
        raise Exception("Error: Numbers cannot be more than four digits")

ops = {
    "+": operator.add,
    "-": operator.sub
}

arithmetic_arranger(["32 + 698", "3801 + 2", "45 - 43", "123 - 49"],False)
