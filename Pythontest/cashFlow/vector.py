
from distutils import sys

class Vector:
    from dateutil.relativedelta import relativedelta
    import datetime

    def __init__(self, closingDate, firstPaymentDate, paymentFreq, dayFactorSys, maturityDate):
        self.ClosingDate = closingDate
        self.FirstPaymentDate = firstPaymentDate
        self.PaymentFreq = paymentFreq
        self.DayFactorSystem = dayFactorSys
        self.MaturityDate = maturityDate

    def BuildVectorHistoryTillMaturityDate(self):
        period = 0
        date = ClosingDate
        nextDate = date
        dayFactor = 0
        vectorHistoryList = []

        while ( date < self.MaturityDate):
            vectorHistory =  VectorHistory(period, date, dayFactor)
            vectorHistoryList.append(vectorHistory) 
            period = period + 1
            date = GetNextDateGivenPaymentFreq(date, PaymentFreq)
            dayFactor = GetDayFactorGivenDayFactorSystem(date, nextDate, DayFactorSystem)
        
        return vectorHistoryList;

class VectorHistory:
    def __init__(self, period, date, dayFactor):
        self.Period = period
        self.Date = date
        self.DayFactor = dayFactor

