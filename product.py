products = []
while True:
	name = input('Please enter the product you buy: ')
	if name == 'q':
		break
	price = input('Please enter the price: ')
	products.append([name, price])
print(products) 