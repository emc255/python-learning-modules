import datetime

if __name__ == '__main__':
    new_time = datetime.time(5, 44, 44, 4)
    print(new_time)
    today = datetime.date.today()
    print(today)
    print(today.ctime())

    date_time = datetime.datetime(2222, 12, 11, 1, 11, 10)
    print(date_time)

    print("SUBTRACTING DATE")
    jennie_date = datetime.date(1996, 1, 16)
    result = today - jennie_date
    print(type(result))
    print(result)
