t = 5
for t in range(t):
    x,y,z = map(int, input().split())

    if x+y == z or x+z == y or y+z == x :
        print("YES")
    else :
        print("NO")
