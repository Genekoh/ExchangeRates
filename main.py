from api import exchangeApi as ex


print("Welcome to Exchange Rates")

print("What would you like to do")

a = ex.convertRates("GBP", "THB")
print(a)
