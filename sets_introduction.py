def average(array):
    sum = 0
    unique_heights = set(array)
    for height in unique_heights:
        sum += int(height)
    average = sum / len(unique_heights)
    return round(average,3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

