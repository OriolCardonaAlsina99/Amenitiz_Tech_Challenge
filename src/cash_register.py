from Product import Product
from rules.check_rules import check_rules
from rules.check_basket import handle_basket

def compute():
    while True:
        print ('| Product Code | Name | Price |') 
        print ('|--|--|--|')
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

        total_price = handle_basket(products, check_rules(products))
        print('| Basket | Total price expected |')
        print('|--|--|')
        print('| ' + ids[:-1] + ' | ' + str(total_price) + '€ |')
        print('\n')
    
compute()