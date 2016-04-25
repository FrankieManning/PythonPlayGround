from math import sqrt, cos
from distutils import sys
import numpy as np
import pandas as pandas
from pandas.core.frame import DataFrame
from numpy.ma import divide

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

if __name__ == "__main__":
    sys.exit(int(myFunction(VecotrCls(0, 365, divide(float(1),365))) or 0))


