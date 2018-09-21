#File created by Yogesh Manghnani

def checkIfLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def getNumberOfDaysMonth(month, year):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leapMonths = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if checkIfLeap(year):
        return leapMonths[month-1]
    else:
        return months[month-1]


def numberOfDaysYear(year):
    if checkIfLeap(year):
        return 366
    else:
        return 365


if __name__ == "__main__":
    numberOfSundays = 0
    start = 2   # year starts at tuesday 2nd day of week
    for year in range(1901, 2001):
        first = start
        for month in range(1, 13):
            if first % 7 == 0:
                numberOfSundays += 1
            first += getNumberOfDaysMonth(month, year) % 7

        start += numberOfDaysYear(year)
        start %= 7


    print(numberOfSundays)
