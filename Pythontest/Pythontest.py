def dateTimeTest():
    from dateutil.relativedelta import relativedelta
    import datetime
    date = datetime.date(2016, 1, 31)
    three_mon_rel = relativedelta(months=1)
    date = three_mon_rel + date
    print date

if __name__ == "__main__":
    dateTimeTest();


