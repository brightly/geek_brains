n = 1
count = 1
products = list()
temp = dict()
while n != -1:
    name = input('Введите название товара')
    price = input('Введите цену товара')
    amount = input('Введите количество')
    quantity = input('Введите единицы измерения')
    print('Если хотите окончить ввод -1, иначе любое число')
    n = int(input())
    products.append(count)
    temp['название'] = name
    temp['цена'] = price
    temp['количество'] = amount
    temp['eд'] = quantity
    products.append(temp)
    count += 1
products = tuple(products)
product = dict()
for i in range(1, len(products),2):
    for key, val in products[i].items():
        if key in product:
            product[key].append(val)
        else:
            product[key] = [val]
print(product)