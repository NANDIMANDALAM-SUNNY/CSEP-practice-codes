
principal=int(input("Enter amount to calculate the compound intrest:"))
rate=int(input("Enter the rate : "))
year=float(input("Enter the years : "))
def compoundIntrest(principal,rate,year):
    if year<=0:
        return principal
    else:
        return compoundIntrest(principal+principal*rate/100,rate,year-1)
print(compoundIntrest(principal,rate,year))
