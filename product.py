product = []
import os
if os.path.isfile('product.cvs'):
	print('yes')
	with open('product.cvs', 'r', encoding='utf-8') as f:
		for s in f:
			if '商品,價格' in s:
				continue
			name, price = s.strip().split(',')
			product.append([name, price])
	print(product)
else:
	print('no')

while True:
	name = input('名稱')
	if name == 'q':
		break
	price = input('價格')
	p = [name, price]
	product.append(p)
	
print(product)
with open ('product.cvs', 'w', encoding='utf-8') as d:
	d.write('商品,價格\n')
	for p in product:
		d.write(p[0] + ',' + p[1] + '\n')