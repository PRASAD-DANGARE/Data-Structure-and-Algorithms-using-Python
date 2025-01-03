def func_lin(lst):
    '''
    Takes in list and prints out all values
    '''
    for val in lst:
        print(val)
        
func_lin([1,2,3])

"""
This function runs in O(n) (linear time). This means that the number of operations taking place scales linearly with n, 
so we can see here that an input list of 100 values will print 100 times, a list of 10,000 values will print 10,000 times, and a list of n values will print n times.
"""