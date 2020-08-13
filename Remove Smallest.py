n = int(input())

l = []

for i in range(n):
    arrSize = int(input())

    a = list(map(int, input().split()))

    if arrSize == 1:
        l.append("YES")
    else:
        a.sort()
        isPossible = True
        for k in range(arrSize - 1):
            if a[k + 1] - a[k] <= 1:
                continue
            else:
                isPossible = False
                break
        if isPossible:
            l.append("YES")
        else:
            l.append("NO")


for s in l:
    print(s)

