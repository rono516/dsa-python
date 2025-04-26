if __name__ == "__main__":
    nums = [3,3,3]
    target = 3

    output = []

    for i in range(len(nums)):
        if nums[i] == target:
            output.append(i)
    if len(output) == 0:
        print([-1,-1])

    elif len(output) == 1:
        output.insert(0,output[0])
        print(output)
    else:
        print([output[0],output[len(output)-1]])