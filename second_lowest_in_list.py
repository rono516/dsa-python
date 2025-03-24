if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr_list = list(arr)
    arr_list.sort(reverse=True)
    firstValue = arr_list[0]
    nextValue= firstValue
    for nom in arr_list:
        if nom < firstValue:
            nextValue = nom
            break

    print(nextValue)


