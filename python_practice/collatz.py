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
    n = arg[0]
    try:
        if n%2==0:
            return n/2
        if n%2==1:
            return (n*3)+1
    except:
        return 'invalid entry'

def masterfunc(*arg):
    x = collatz(arg[0])
    output=[x]
    if isinstance(x, int):
        while x !=1:
            x=collatz(x)
            output.append(x)
        return output
    else:
        return output

# Test with appropriate inputs
if __name__=='__main__':
    for arg in [12, 19, 'foobar']:
        output = masterfunc(arg)
        print(arg, output)
