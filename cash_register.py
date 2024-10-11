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
    if (len(green_teas) < 2):
        return price
    if(len(green_teas)%2 == 0):
        return price/2
    else:
        green_tea_price = green_teas[0].getPrice()
        size_arr = len(green_teas) - 1
        return ((green_tea_price*size_arr)/2 + green_tea_price)

def COO_rule(products):
    strawberries = []
    price = 0
    final_price = 0
    for p in products:
        if(p.getId() == 'SR1'):
            strawberries.append(p)
            price += p.getPrice()
    size_arr = len(strawberries)
    if (size_arr  < 3): 
        return price
    else: 
        strawberries_price = strawberries[0].getPrice()
        while(size_arr%3 != 0):
            size_arr -= 1
            final_price += strawberries_price
        final_price += 4.5*3*(size_arr/3)
        return final_price
    
def VP_rule(products):
    coffies = []
    price = 0
    final_price = 0
    for p in products:
        if(p.getId() == 'CF1'):
            coffies.append(p)
            price += p.getPrice()
    size_arr = len(coffies)
    if (size_arr  < 3): 
        return price
    else: 
        coffies_price = coffies[0].getPrice()
        while(size_arr%3 != 0):
            size_arr -= 1
            final_price += coffies_price
        final_price += (coffies_price*size_arr*2)/3
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
price_rule2 = COO_rule(products)
total_price += price_rule2
price_rule3 = VP_rule(products)
total_price += price_rule3
print_total(products, total_price)