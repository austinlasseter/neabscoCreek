def myfunc(*arg):
    '''
    Summary: find the first number in a list that doesn't occur twice.

    Parameters: list.
    Returns: integer.
    '''
    uniques=list(set(arg[0]))
    repeat_d={}
    for i in uniques:
        repeat_d[i]=0
    for j in arg[0]:
        repeat_d[j]+=1
    # returnlist=[]
    # for k in repeat_d.keys():
    #     if repeat_d[k]==1:
    #         returnlist.append(k)
    return [k for k in repeat_d.keys() if repeat_d[k]==1][0]


if __name__=='__main__':
    arg=[6, 5, 3, 5, 4, 3, 2, 7, 4, 6]
    print(myfunc(arg))
