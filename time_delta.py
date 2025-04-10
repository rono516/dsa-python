from datetime import datetime
    
def time_delta(t1, t2):
    t1 = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2 = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")

    time_diff = t2-t1
    diff_in_seconds = time_diff.total_seconds()
    diff_in_seconds = f"{diff_in_seconds:.0f}"
    diff_in_seconds = diff_in_seconds.strip("-")
    diff_in_seconds = diff_in_seconds.strip("+")

    # print(diff_in_seconds)
    return diff_in_seconds

if __name__ == '__main__':

    t = int(input())

    differences = []

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        differences.append(delta)
    for difference in differences:
        print(difference)
