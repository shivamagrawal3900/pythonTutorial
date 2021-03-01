amount = int(input("Enter the amount: "))

remaining_amount = amount

currency = 2000
notes = remaining_amount // currency
print(currency, "\t * ", notes)
remaining_amount = remaining_amount % currency

currency = 500
notes = remaining_amount // currency
print(currency, "\t * ", notes)
remaining_amount = remaining_amount % currency

currency = 200
notes = remaining_amount // currency
print(currency, "\t * ", notes)
remaining_amount = remaining_amount % currency

currency = 100
notes = remaining_amount // currency
print(currency, "\t * ", notes)
remaining_amount = remaining_amount % currency

currency = 50
notes = remaining_amount // currency
print(currency, "\t\t * ", notes)
remaining_amount = remaining_amount % currency

currency = 20
notes = remaining_amount // currency
print(currency, "\t\t * ", notes)
remaining_amount = remaining_amount % currency

currency = 10
notes = remaining_amount // currency
print(currency, "\t\t * ", notes)
remaining_amount = remaining_amount % currency

currency = 2
notes = remaining_amount // currency
print(currency, "\t\t * ", notes)
remaining_amount = remaining_amount % currency

currency = 1
notes = remaining_amount // currency
print(currency, "\t\t * ", notes)
remaining_amount = remaining_amount % currency
