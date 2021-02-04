for t in range(int(input())):
    n = int(input())
    arr = [1 for i in range(n+1)]
    arr = map(int,input().split())
    total = sum(arr)

    if total % 2 == 0 :
        print("1")
    else :
        print("2")
