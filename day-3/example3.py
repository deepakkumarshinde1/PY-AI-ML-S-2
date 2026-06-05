# 100
# 5% 
# 1 Year
# 105

# p
# r
# t

#si = (p * r * t)/100
principal = int(input("Enter Principal Amount = "))
rateOfInterest = float(input("Enter Rate of interest = "))
time = int(input("Enter Time In Years = "))

si = (principal * rateOfInterest * time) / 100

print("The simple interest for given values is = ",si)
