from math import sqrt, cos
from distutils import sys
import numpy as np
import pandas as pandas
from pandas.core.frame import DataFrame
from numpy.ma import divide
from cashFlow.datesTiming import dayFactorSys

class VecotrCls:
   def __init__(self, closingDate, maturityDate, dayFactor):
       self.MaturityDate = maturityDate
       self.ClosingDate = closingDate
       self.DayFactor = dayFactor

def myFunction(vectorObj):
    addedDays = vectorObj.DayFactor * 365
    nextDay = vectorObj.ClosingDate
    PaymentDays = [];
    while nextDay < vectorObj.MaturityDate :
        nextDay = nextDay + addedDays;
        PaymentDays.append(nextDay);

    PaymentDaysDic = { 'Payment Days' : PaymentDays}
    t1 = DataFrame.from_records(data=PaymentDaysDic, index=None); 
    print t1;

def test():
    t= "sd";
    print t;
    t =  [1,2];
    print t;
    t="mahshd";
    print t;

def dateTimeTest():
    from dateutil.relativedelta import relativedelta
    import datetime
    date = datetime.date(2016, 1, 31)
    three_mon_rel = relativedelta(months=1)
    date = three_mon_rel + date
    print date

if __name__ == "__main__":
    dateTimeTest();


