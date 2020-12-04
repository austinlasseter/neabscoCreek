def countdown(num):
    outputlist=[]
    for i in range(num, -1, -1):
        outputlist.append(str(num-i))
    output=''.join(outputlist)
    print(output[1:])


if __name__=="__main__":
    countdown(5)
