#mac_produce

product = []
while True:
	name =  input('請輸入餐點：')
	if name == 'q':
		break
	price = input('請輸入價格：')
	product.append([name, price])
print(product[0])

for p in product:
	print(p[0], '價格是', p[1])