from Product import Product

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
    prod = Product(identifier, prod_name, prod_price)
    print('| ' + prod.getId() + ' | ' + prod.getName() + ' | ' + prod.getPrice() + ' |')