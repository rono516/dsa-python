# from math import sqrt
# if __name__ == "__main__":
#     a = 10
#     b = 10
#     hypotenuse = a*a + b*b
#     print(sqrt(hypotenuse))


# leetcode problem - https://leetcode.com/problems/search-in-rotated-sorted-array/description/

if __name__ == "__main__":
    nums =[4,5,6,7,0,1,2]
    target = 0
    location = None

    # if target in nums:
    #     print("There")
    # else :
    #     print("Not there")

    for i in range(len(nums)):
        if nums[i] == target:
            location = i

    if location:
        print(location)
    else:
        print(-1)


    
