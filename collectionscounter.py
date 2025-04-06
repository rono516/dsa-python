from collections import Counter
if __name__ == "__main__":
    number_of_shoes = int(input("Number of shoes "))
    all_shoe_sizes = input("All shoe sizes ").split(" ")
    number_of_customers = int(input("Number of customers "))
    money_earned = 0
    order_size_and_price = []
    max_count_of_sizes_ordered = 2

    for i in range(number_of_customers):
        order_size, order_price = input().split(" ")
        order_size_and_price.append([order_size,order_price])

    sizes_ordered = []

    for order in order_size_and_price:
        count = Counter(sizes_ordered)

        if count[order[0]] < 2:
            if order[0] in all_shoe_sizes:
                sizes_ordered.append(order[0])
                money_earned += int(order[1])
    print(money_earned)

