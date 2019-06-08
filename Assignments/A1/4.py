amount = int(input('Enter amount in cent: '))
dollar = amount // 100
amount %= 100
quaters = amount // 25
amount %= 25
dimes = amount // 10
amount %= 10
nickels = amount // 5
amount %= 5
pennies = amount
print(f'Amount: {dollar} dollars {quaters} quaters {dimes} dimes {nickels} nickels {pennies} pennies')
