from Product import Product
from ceo_rule import CEO_rule

def print_total (products, total_price):
    print('| Basket | Total price expected |')
    print('|--|--|')
    products_codes = ''
    for p in products:
        products_codes = products_codes + p.getId() + ','
        if (p.getId() != 'GR1' and p.getId() != 'SR1' and p.getId() != 'CF1'):
            total_price += p.getPrice()
            print(total_price)
    print('| ' + products_codes[:-1] + ' | ' + str(total_price) + '€ |')

def COO_rule(products):
    price = 0
    final_price = 0
    for p in products:
        price += p.getPrice()
    size_arr = len(products)
    if (size_arr  < 3): 
        return price
    else: 
        strawberries_price = products[0].getPrice()
        while(size_arr%3 != 0):
            size_arr -= 1
            final_price += strawberries_price
        final_price += 4.5*3*(size_arr/3)
        return final_price
    
def VP_rule(products):
    price = 0
    final_price = 0
    for p in products:
        price += p.getPrice()
    size_arr = len(products)
    if (size_arr  < 3): 
        return price
    else: 
        coffies_price = products[0].getPrice()
        while (size_arr%3 != 0):
            size_arr -= 1
            final_price += coffies_price
        final_price += (coffies_price*size_arr*2)/3
        return final_price
    
def check_rules(products):
    green_teas = []
    strawberries = []
    coffies = []
    for p in products:
        if (p.getId() == 'GR1'):
            green_teas.append(p)
        if (p.getId() == 'SR1'):
            strawberries.append(p)
        if (p.getId() == 'CF1'):
            coffies.append(p)
    price_rule1 = CEO_rule(green_teas)
    price_rule2 = COO_rule(strawberries)
    price_rule3 = VP_rule(coffies)
    total_price = price_rule1 + price_rule2 + price_rule3
    return total_price

def compute():
    while True:
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
            print('| ' + product.getId() + ' | ' + product.getName() + ' | ' + str(product.getPrice()) + '€ |')
            products.append(product)

        total_price += check_rules(products)
        print_total(products, total_price)
        print('\n')
    
compute()