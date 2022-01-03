import Stack
def par_check(symbol_string):
    s= Stack()
    balence=True
    index=0
    while index<len(symbol_string) and balence:
        symbol=symbol_string[index]
        if symbol=="(":
            s.push(symbol)
        else:
            if s.is_empty():
                balence=False
            else:
                 s.pop()
                 index=index+1
    if balence and s.is_empty():
        return  True
    else:
        return False
print(par_check('((()))'))