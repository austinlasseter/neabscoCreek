# Function
def collatz(*arg):
    '''
    Summary: Write a Python program where you take any positive integer n,
        * if n is even, divide it by 2 to get n / 2.
        * If n is odd, multiply it by 3 and add 1 to obtain 3n + 1.
        * Repeat the process until you reach 1.
    Parameters: any positive integer n
    Returns: List of Collatz permutations, ending in 1
    '''
    return arg[0]


# Test with appropriate inputs
if __name__=='__main__':
    for arg in [12, 19, 'foobar']:
        output = collatz(arg)
        print(arg)
        print(output)
