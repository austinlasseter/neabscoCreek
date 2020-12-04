
def runnerup(*args):
    list1=list(args[1])
    top=max(list1)
    list2 = [i for i in list1 if i < top]
    print(max(list1))

if __name__ == '__main__':
    runnerup(5, [1,2,3,4,5,5])
