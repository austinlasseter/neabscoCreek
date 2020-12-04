

def fizzbuzz(num):
    '''
    For multiples of three print "Fizz" instead of the number and
    for the multiples of five print "Buzz".
    For numbers which are multiples of both three and five print "FizzBuzz".
    '''
    if num%3==0:
        print(str(num) + ' fizz')
    if num%5==0:
        print(str(num) + ' buzz')
    if (num%3==0) & (num%5==0):
        print(str(num) + ' fizzbuzz')
    else:
        print(num)

if __name__=='__main__':
    for num in range(50):
        fizzbuzz(num)
