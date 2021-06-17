products = []
while True:
	n = input('請輸入商品名稱: ')
	if n == 'q':
		break
	price = input('請輸入商品價格: ')
	products.append([n, price])
print(products)