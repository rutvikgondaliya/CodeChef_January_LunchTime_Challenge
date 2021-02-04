for t in range(int(input())):
    n = int(input())
    odd = 0
    even = 0
    for i in range(1,n+1):
        arr = int(input())
        if arr % 2 == 1:
            odd += 1
        else :
            even += 1
    print(min(odd,even))
