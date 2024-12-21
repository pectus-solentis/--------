def math_func1(x,y,op):

    def add_():
        return x+y
    def sub_():
        return x-y
    def mul_():
        return x*y
    def div_():
        return x/y
    
    op_func = {'+':add_, '-':sub_, '*':mul_, '/':div_}.get(op,add_)
    return op_func()

print(math_func1(5,5,'+'))
print(math_func1(5,5,'-'))
print(math_func1(5,5,'*'))
print(math_func1(5,5,'/'))