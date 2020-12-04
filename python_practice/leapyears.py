def leapyear(n):
    if (n%400==0):
        return(True)
    elif (n%100==0):
        return(False)
    elif (n%4==0):
        return(True)
    else:
        return(False)

if __name__=='__main__':
    x = leapyear(1900)
    print(x)
