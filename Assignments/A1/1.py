cover_price = 24.95
discount_price = cover_price - (0.4 * cover_price)
wholesale_price = discount_price + 3
wholesale_price += (discount_price + 0.75) * 59
print('Wholesale price for 60 copies: ', wholesale_price)
