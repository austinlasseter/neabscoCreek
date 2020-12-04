def maxcharacter(s):
    counts={}
    for element in s:
        if element in counts:
            counts[element]+=1
        else:
            counts[element]=1
    results=[]
    for item in counts.items():
        if item[1]==max(counts.values()):
            results.append(item[0])
    results.sort()
    print(results[0])

    # print(max(counts.values()))
    # print(counts.items())

if __name__=='__main__':
    maxcharacter('hellosthisissomuchfunthisissomichfun')
