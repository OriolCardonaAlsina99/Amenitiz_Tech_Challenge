from Product import Product

def print_total (products, total_price):
    print('| Basket | Total price expected |')
    print('|--|--|')
    products_codes = ''
    for p in products:
        products_codes = products_codes + p.getId() + ','
    print('| ' + products_codes[:-1] + ' | ' + str(total_price) + ' |')


print ('| Product Code | Name | Price |')
print ('|--|--|--|')
products = []
total_price = 0
while True:
    identifier = input()
    prod_name = input()
    prod_price = input()
    if((identifier or prod_name or prod_price) == ''):
        break
    product = Product(identifier, prod_name, float(prod_price))
    print('| ' + product.getId() + ' | ' + product.getName() + ' | ' + str(product.getPrice()) + ' |')
    products.append(product)
    total_price += product.getPrice()
print_total(products, total_price)