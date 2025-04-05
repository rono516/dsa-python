if __name__== "__main__":
    happiness = 0
    # array_of_n_integers = []
    NM = input("N and M ")
    N, M = NM.split(" ")
    N= int(N)
    M= int(M)
    elements_of_array = input("Elements ").split(" ")
    elements_of_array = elements_of_array[:N]
    likeables = input("Liked Integers ").split(" ")
    likeables = set(likeables[:M])

    unlikeables = input("UnLiked Integers ").split(" ")
    unlikeables = set(unlikeables[:M])

    # print(likeables)
    for number in likeables:
        if number in elements_of_array:
            happiness +=1
    if happiness> 0:
        for number in unlikeables:
            if number in elements_of_array:
                happiness -=1
    print(happiness)