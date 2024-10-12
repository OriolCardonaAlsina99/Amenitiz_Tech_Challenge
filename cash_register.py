from Product import Product
from ceo_rule import CEO_rule
from vp_rule import VP_rule
from coo_rule import COO_rule

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