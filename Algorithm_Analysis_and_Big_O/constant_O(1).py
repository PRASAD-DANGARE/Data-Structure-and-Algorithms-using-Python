def func_constant(values):
    '''
    Prints first item in a list of values.
    '''
    print(values[0])
    
func_constant([1,2,3])

"""
Note how this function is constant because regardless of the list size, the function will only ever take a constant step size, 
in this case 1, printing the first value from a list. so we can see here that an input list of 100 values will print just 1 item, 
a list of 10,000 values will print just 1 item, and a list of **n** values will print just 1 item!
"""