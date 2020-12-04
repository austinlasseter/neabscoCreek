def students(*args):
    students=args[0][0]
    subjects=args[0][1]
    for i in range(1, subjects+1):
        ave=sum(args[i])/len(args[i])
        print (ave)

if __name__=='__main__':
    n, x = map(int, input().split())
    students(n,x)
