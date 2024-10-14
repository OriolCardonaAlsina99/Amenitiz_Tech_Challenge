from modules.Product import Product
from modules.check_rules import handle_rules
from modules.check_basket import handle_basket

def close_program(id, name):
    if (id != 'close_cash_register' and name != 'close_cash_register'):
        return False
    else:
        return True

def price_is_float(price):
    try:
        float(price)
        return True
    except ValueError:
        return False

def compute():
    identifier = None
    prod_name = None
    prod_price = 0.0
    while not close_program(identifier, prod_name):
        if(identifier != '' and prod_name != '' and prod_price != ''):
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
            if(price_is_float(prod_price)):
                product = Product(identifier, prod_name, float(prod_price))
                print('| ' + product.getId() + ' | ' + product.getName() + ' | ' + str(product.getPrice()) + '€ |')
                products.append(product)
                ids += product.getId() + ','
            else:
                print("Price must be a number")

        total_price = handle_basket(products, handle_rules(products))
        if not close_program(identifier, prod_name):
            print('| Basket | Total price expected |')
            print('|--|--|')
            print('| ' + ids[:-1] + ' | ' + str(total_price) + '€ |')
    
compute()