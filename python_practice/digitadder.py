def myfunc(*arg):
    '''
    Summary: add the digits of a positive integer repeatedly until result has single digit

    Parameters: single integer.
    Returns: integer.
    '''
    if isinstance(arg[0], int):
        if (len(str(arg[0]))==1) | (len(str(arg[0]))>2):
            return 'please input integer with 2 digits'
        else:
            d1=int(str(arg[0])[0])
            d2=int(str(arg[0])[1])
            sumd1d2 = d1+d2
            if len(str(sumd1d2))==1:
                return sumd1d2
            else:
                f1=int(str(sumd1d2)[0])
                f2=int(str(sumd1d2)[1])
                sumf1f2 = f1+f2
                if len(str(sumf1f2))==1:
                    return sumf1f2
                else:
                    'this is taking too long'

    else:
        return 'please input integer'

if __name__=='__main__':
    for arg in [59, 48, 99, 12, 6, 333, 'cow']:
        print(myfunc(arg))
