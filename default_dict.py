from collections import defaultdict

if __name__ == "__main__":
    A, B = input().split(" ")
    A = int(A)
    B = int(B)

    initial_list = []
    values_to_check_in_initial_list = []

    for _ in range(A):
        value = input()
        initial_list.append(value)

    for _ in range(B):
        value  = input()
        values_to_check_in_initial_list.append(value)


    # checking_dict = defaultdict(int)

    for value in values_to_check_in_initial_list:
        # checking_dict[value] +=1
        if value  not in initial_list:
            print("-1", end=" ")
        else:
            indexes = [i+1 for i, x in enumerate(initial_list) if x==value ] 
            for index in indexes:
                print(index, end=" ")
        print()

    # print(checking_dict)
        




# d = defaultdict(list)

# d["python"].append("awesome")
# d["something-else"].append("not relevant")
# d["python"].append("language")
# for i in d.items():
#     print (i)

# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

