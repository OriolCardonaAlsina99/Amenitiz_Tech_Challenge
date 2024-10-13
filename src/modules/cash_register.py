from modules.Product import Product
from modules.check_rules import handle_rules
from modules.check_basket import handle_basket

def close_program(id, name, price):
    if (id != 'close_cash_register' and name != 'close_cash_register' and price != 'close_cash_register'):
        return False
    else:
        return True

def compute():
    identifier = ''
    prod_name = ''
    prod_price = ''
    while not close_program(identifier, prod_name, prod_price):
        print('| Product Code | Name | Price |') 
        print('|--|--|--|')
        products = []
        ids = ''
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
            ids += product.getId() + ','

        rules_prices = handle_rules(products)
        total_price = handle_basket(products, rules_prices)
        print('| Basket | Total price expected |')
        print('|--|--|')
        print('| ' + ids[:-1] + ' | ' + str(total_price) + '€ |')
        print('\n')
    
compute()