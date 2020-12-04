def nonrepeatingCharacter(s):
    #code here

    counts={}
    for element in s:
        if element in counts:
            counts[element]+=1
        else:
            counts[element]=1

    output=[]
    for element in s:
        if counts[element]==1:
            output.append(element)
    testlist=[]
    print(len(testlist))
    print(str(output[0]))
    return str(output[0])

if __name__=='__main__':
    nonrepeatingCharacter('hello')
