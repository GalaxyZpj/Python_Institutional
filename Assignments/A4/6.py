prices = {
    "banana": [4, 1],
	"apple": [2, 2],
	"orange": [1.5, 3],
	"pear": [3, 4]
}
total = 0
for x in prices.keys():
    print(f'{x}: \nPrice: {prices[x][0]}\nStock: {prices[x][1]}\n\n')
    total += prices[x][0]*prices[x][1]
print('Total amount earned: ', total)
