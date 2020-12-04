def roman(num):
    romansdict={'I':1, 'V':5, 'X':10}
    output=0
    if len(num)==1:
        output+=romansdict[num[0]]
    else:
        for i in range(len(num)-1):
            if num[i]<num[i+1]:
                output-=romansdict[num[i]]
            if num[i]>num[i+1]:
                output+=romansdict[num[i]]
            if num[i]==num[i+1]:
                output+=romansdict[num[i]]
        output+=romansdict[num[-1]]
    return output


if __name__=='__main__':
    output = roman('XVII')
    print(output)
