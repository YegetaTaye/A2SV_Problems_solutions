def countSwaps(a):
    countswaps = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                countswaps += 1
    print(f"Array is sorted in {countswaps} swaps.")
    print("First element: ", a[0])
    print("Second element: ", a[-1])


n = int(input().strip())
a = list(map(int, input().rstrip().split()))

countSwaps(a)
