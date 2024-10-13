def handle_basket (products, total_price):
    print('| Basket | Total price expected |')
    print('|--|--|')
    products_codes = ''
    for p in products:
        products_codes = products_codes + p.getId() + ','
        if (p.getId() != 'GR1' and p.getId() != 'SR1' and p.getId() != 'CF1'):
            total_price += p.getPrice()
    print('| ' + products_codes[:-1] + ' | ' + str(total_price) + '€ |')