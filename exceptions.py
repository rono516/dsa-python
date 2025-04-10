if __name__ == "__main__":
    no_of_values = int(input())
    operating_values = []

    for _ in range(no_of_values):
        no1, no2 =  input().split(" ")
        operating_values.append([no1,no2])
    for operation in operating_values:
        try:
            result = int(operation[0]) // int(operation[1])
            print(result)
        except Exception as e:
            print(f"Error Code: {e}")

