def findNumber(arr, n, k):
    if k not in arr:
        print(-1)
    else:
        print(arr[k])



if __name__=='__main__':
    N = 9
    myarray = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    K = 30
    findNumber(myarray, N, K)
