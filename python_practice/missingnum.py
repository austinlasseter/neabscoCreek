def missnum(numlist):
    '''
    Write a Python program to find a missing number from a list.
    '''
    missing=[]
    full_list=[i for i in range(1, max(numlist))]
    for i in full_list:
        if i not in numlist:
            missing.append(i)
    return missing

if __name__=='__main__':
    l = [1,2,3,4,6,7,8]
    print(missnum(l))
