import calendar

if __name__ == "__main__":
    month, day , year = map(int, input().split())
    weekday = calendar.weekday(year=year,month=month,day=day)
    match weekday:
        case 0:
            print("MONDAY")
        case 1:
            print("Tuesday".upper())
        case 2:
            print("Wednesday".upper())
        case 3:
            print("Thursday".upper())
        case 4:
            print("Friday".upper())
        case 5:
            print("Saturday".upper())
        case 6:
            print("Sunday".upper())
        case _:
            print("Invalid".upper())

