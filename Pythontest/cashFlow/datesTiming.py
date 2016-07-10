from enum import Enum
from dateutil import relativedelta

class DayFactorSystem(Enum):
    Thirty360 = 0
    Actual360 = 1
    ActualActual = 2
    
class PaymentFreqSystem(Enum):
    Monthly = 0
    Quarterly = 1
    SemiAnnual = 2
    Annual = 3

def GetNextDateGivenPaymentFreqSystem(date, paymentFreq):
    monthsToBeAdded = relativedelta(months=paymentFreq)
    nextDate = date + monthsToBeAdded

def GetDayFactorGivenDayFactorSystem(startDate, endDate, dayFactorSys):
    dayFactor = 0
    if dayFactorSys == DayFactorSystem.Thirty360:
        dayFactor = Days360(startDate, endDate)
    elif dayFactorSys == DayFactorSystem.Actual360:
        dayFactor = GetDayFactorForActual360(startDate, endDate)
    elif dayFactorSys == DayFactorSystem.ActualActual:
        dayFactor = GetDayFactorForActualActual(startDate, endDate)
    return dayFactor;


def Days360(startDate, endDate, method):
    dayFactor = 0
    if method == True:
        dayFactor = Days360EU(startDate, endDate)
    else:
        dayFactor = Days360US(startDate, endDate)
    return dayFactor;
 
def Days360US(startDate, endDate):
    dayFactor = 0;
    endDateDay = 0;
    startDateDay = 0;
    deltaMonthsBetweenStartDateEndDat = 0;

    if (isLastDayOfMonth(endDate)):
        endDateDay = 30
    else:
        endDateDay = endDate.day
    if (isLastDayOfMonth(startDate)):
        startDateDay = 30
    else:
        startDateDay = startDate.day
    if startDateDay < endDateDay:
        deltaMonthsBetweenStartDateEndDat = ( endDate - startDate ).months - 1  
    else:
        deltaMonthsBetweenStartDateEndDat = ( endDate - startDate ).months
        
    dayFactor = deltaMonthsBetweenStartDateEndDat * 30 + 30 - startDate.day + endDate.day

    return dayFactor;

#def Days360EU(startDate, endDate):
def GetDayFactorForActual360(startDate, endDate):
    dayFactor = 0;
    dayFactor = ( startDate- endDate ).days/360

    return dayFactor;

def GetDayFactorForActualActual(startDate, endDate):
    dayFactor = 0;
    dayFactor = ( startDate- endDate ).days/365

    return dayFactor;

