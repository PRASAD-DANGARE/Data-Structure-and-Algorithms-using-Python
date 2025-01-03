def cubic_example(lst):
    '''
    Example of cubic complexity
    '''
    for i in lst:          # O(n)
        for j in lst:      # O(n)
            for k in lst:  # O(n)
                print(i, j, k)  # O(1) operation

lst = [1, 2, 3]
cubic_example(lst)

"""
If an algorithm processes all combinations of three elements from the input or involves three levels of nested iteration, it is likely 
o(n3)

Typically involves three nested loops, each iterating over the input, or scenarios requiring three levels of interaction.
"""