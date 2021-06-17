products = []
while True:
	n = input('請輸入商品名稱: ')
	if n == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([n, price])
for p in products:
	print(p[0], '的價格是', p[1], '元')