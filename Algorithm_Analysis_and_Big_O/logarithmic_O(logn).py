# Any algorithm that repeatedly halves the input size exhibits logarithmic complexity
def func_log(n):
    '''
    Prints n, then repeatedly halves n until it becomes 0
    '''
    while n > 0:
        print(n)
        n = n // 2
 
# Example
func_log(16)

"""
The input size is repeatedly reduced by a constant factor (e.g., divided by 2) at each step
Logarithmic algorithms are highly efficient, especially for large inputs, as the runtime grows very slowly.
"""