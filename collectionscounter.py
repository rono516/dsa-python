from collections import Counter

if __name__ == "__main__":
    number_of_shoes = int(input())
    all_shoe_sizes = input().split(" ")
    number_of_customers = int(input())
    money_earned = 0
    order_size_and_price = []

    for _ in range(number_of_customers):
        order_size, order_price = input().split(" ")
        order_size_and_price.append([order_size,order_price])

    count = Counter(all_shoe_sizes)

    for order in order_size_and_price:
        if count[order[0]] > 0:
            if order[0] in all_shoe_sizes:
                money_earned += int(order[1])
                count[order[0]] -=1
    print(money_earned)

