# def name(funC):
#     def printfun():
#         funC()
#         x= funC()
#         y=x*5
#         print(y)
#         return printfun
    
#     name()
    
    
    
    
def outer_function(x):
    def inner_function(y):
        return x + y

    result = inner_function(5)
    return result

# Example usage:
outer_result = outer_function(10)
print(outer_result)