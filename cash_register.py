from Product import Product

def print_total (products, total_price):
    print('| Basket | Total price expected |')
    print('|--|--|')
    products_codes = ''
    for p in products:
        products_codes = products_codes + p.getId() + ','
    print('| ' + products_codes[:-1] + ' | ' + str(total_price) + ' |')

def CEO_rule (products):
    green_teas = []
    price = 0
    for p in products:
        if(p.getId() == 'GR1'):
            green_teas.append(p)
            price += p.getPrice()
    if(len(green_teas)%2 == 0):
        return price/2
    else:
        green_tea_price = products[0].getPrice()
        size_arr = len(green_teas) - 1
        final_price = (green_tea_price*size_arr)/2 + green_tea_price
        return final_price

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

price_rule1 = CEO_rule(products)
total_price += price_rule1
print_total(products, total_price)