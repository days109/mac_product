#mac_produce
import os
product = []
if os.path.isfile('product.csv'):
	#load
	with open('product.csv', 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			(name, price)= line.strip().split(',')
			product.append([name, price])
else:
	print('無之前紀錄')
#enter
while True:
	name =  input('請輸入餐點：')
	if name == 'q':
		break
	price = int(input('請輸入價格：'))
	product.append([name, price])
print(product[0])

for p in product:
	print(p[0], '價格是', p[1])
#write
with open('product.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品' + ',' + '價格' + '\n')
	for p in product:
		f.write(p[0] + ',' + str(p[1]) +'\n' )
