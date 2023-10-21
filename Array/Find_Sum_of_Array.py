def _sum(arr):
    sum = 0
    for i in arr:
        sum = sum + i
    return sum
if __name__ == "__main__":
    arr = [1,5,9,12]
    n = len(arr)
    result = _sum(arr)
    print("Sum of the array is: ", result)
