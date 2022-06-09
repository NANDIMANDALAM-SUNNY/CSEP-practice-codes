def compoundIntrest(principal, rate, time):
    if time == 1:
        return principal
    else:
        return principal + compoundIntrest(principal, rate, time - 1) * (1 + rate)
principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = int(input("Enter the time in years: "))
print("The compound interest is", compoundIntrest(principal, rate, time))