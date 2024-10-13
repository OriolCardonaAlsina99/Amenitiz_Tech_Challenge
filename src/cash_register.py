from Product import Product
from rules.check_rules import check_rules

def print_total (products, total_price):
    print('| Basket | Total price expected |')
    print('|--|--|')
    products_codes = ''
    for p in products:
        products_codes = products_codes + p.getId() + ','
        if (p.getId() != 'GR1' and p.getId() != 'SR1' and p.getId() != 'CF1'):
            total_price += p.getPrice()
    print('| ' + products_codes[:-1] + ' | ' + str(total_price) + '€ |')

def compute():
    while True:
        print ('| Product Code | Name | Price |') 
        print ('|--|--|--|')
        products = []
        while True:
            identifier = input()
            if(identifier == ''):
                break
            prod_name = input()
            if(prod_name == ''):
                break
            prod_price = input()
            if(prod_price == ''):
                break
            product = Product(identifier, prod_name, float(prod_price))
            print('| ' + product.getId() + ' | ' + product.getName() + ' | ' + str(product.getPrice()) + '€ |')
            products.append(product)

        print_total(products, check_rules(products))
        print('\n')
    
compute()