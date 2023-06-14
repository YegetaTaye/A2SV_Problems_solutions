# Complete the 'insertionSort1' function below.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr

def insertionSort(arr, n):

    for i in range(1, n):
        key = arr[i]
        j = i-1

        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(*arr)


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))

insertionSort(arr, n)
