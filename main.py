# from math import sqrt
# if __name__ == "__main__":
#     a = 10
#     b = 10
#     hypotenuse = a*a + b*b
#     print(sqrt(hypotenuse))


# leetcode problem - https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# study for binary search - https://www.geeksforgeeks.org/python-program-for-binary-search/

def binary_serach(array,low, high,x):
    pass


if __name__ == "__main__":
    nums =[4,5,6,7,0,1,2]
    target = 0
    location = -1
    low = 0
    high = len(nums) -1

    if high >= low:
        mid = (high+low) //2
        if nums[mid] == target:
            location = mid

    else:
        location == -1


    
