if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]

    location = -1

    target = 6

    for i in range(len(nums)):
        if nums[i] == target:
            location = i

    print(location)