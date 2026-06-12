# calc salary

monthSalary = 18000
presentDays = 25

def calcSalary(monthPay,presentDays):
    perDay = monthPay / 30
    salaryToPay = perDay * presentDays
    return salaryToPay

print(calcSalary(monthSalary,presentDays))
print(calcSalary(monthSalary,20))
print(calcSalary(monthSalary,30))


tm = 750
gm = 450

def calcPercentage(total,gain):
    percent = (gain/total)*100
    print(percent)

calcPercentage(tm,gm)