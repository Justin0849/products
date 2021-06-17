products = []
with open ('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #繼續
		n, price = line.strip().split(',')
		products.append([n, price])
print(products)

while True:
	n = input('請輸入商品名稱: ')
	if n == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([n, price])
for p in products:
	print(p[0], '的價格是', p[1], '元')
with open('products.csv', 'w', encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')