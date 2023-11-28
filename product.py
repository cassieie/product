product = []
while True:
	name = input('名稱')
	if name == 'q':
		break
	price = input('價格')
	p = [name, price]
	product.append(p)
	
print(product)