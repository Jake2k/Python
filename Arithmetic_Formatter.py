import operator

ops = {
    "+": operator.add,
    "-": operator.sub
}   
answers =""

def arithmetic_arranger(lista,answers):
    test = []
    for equation in lista:
        listb = equation.split(" ")
        op_func = set_symbol(listb[1])
        answer = op_func(int(listb[0]),int(listb[2]))
        formatted_result = build_result(listb[0],listb[2],listb[1],answer)
        print (formatted_result)
    
def set_symbol(symbol):
    op_func = ops[symbol]
    return op_func
    
def build_result(top_bit,middle_bit,symbol,answer):
    formatted_result = top_bit + "\n" + symbol + " " + middle_bit + "\n" + "-----" + "\n" + str(answer) + "\n"    
    return formatted_result
    
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],answers)






