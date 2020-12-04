def cuboid (x,y,z,n):
    # print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

    mylist=[]
    for c in range(z+1):
        for b in range(y+1):
            for a in range(x+1):
                if a + b + c != n:
                    mylist.append([a,b,c])
    return mylist

if __name__ == '__main__':
    x = 1
    y = 1
    z = 2
    n = 2
    output = cuboid (x,y,z,n)
    print(output)
