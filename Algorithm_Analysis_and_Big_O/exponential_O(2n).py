def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example
print(fibonacci(5))  # Output: 5

"""
the growth rate of their runtime doubles with each additional input element. 
This is one of the fastest-growing complexities and becomes infeasible for large input sizes.
1:2
2:4
3:8
4:16

Exponential algorithms often involve recursive functions that call themselves multiple times for each level of the problem.
"""