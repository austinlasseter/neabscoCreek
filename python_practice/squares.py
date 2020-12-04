def squares(n):
    mylist=[]
    for x in (range(n)):
        mylist.append(x*x)
    for y in mylist:
        print(y)


if __name__=='__main__':
    squares(5)
