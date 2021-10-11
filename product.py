#File Read
products = []
with open('product.csv', 'r', encoding='utf-8')as f:
	for line in f:
		if '商品' in line:
			continue
		s = line.strip().split(',')
		name = s[0]
		price = s[1]
		products.append([name, price])

#User input
while True:
	name = input('Please enter the product you buy: ')  
	if name == 'q':
		break
	price = input('Please enter the price: ')
	products.append([name, price])
print(products) 

#File save
with open('product.csv', 'w', encoding='utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')