n = int(input())

ansList = []

for _ in range(n):
    arrSize = int(input())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    aMin = min(a)
    bMin = min(b)

    counter = 0

    for i in range (arrSize - 1, -1, -1):

        aDiff = a[i] - aMin
        bDiff = b[i] - bMin

        if aDiff > bDiff:
            counter += bDiff
            counter += a[i] - bDiff - aMin
        elif bDiff > aDiff:
            counter += aDiff
            counter += b[i] - aDiff - bMin
        else:
            counter += aDiff

    ansList.append(counter)

for s in ansList:
    print(s)