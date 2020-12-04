def minnumber(arr):
    x = sum(arr)%2
    if x ==0:
        return 2
    else:
        return 1

if __name__=='__main__':
    arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
    x = minnumber(arr)
    print(x)
