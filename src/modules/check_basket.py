def handle_basket (products, total_price):
    special_products = ['GR1', 'SR1', 'CF1']
    for p in products:
        if (p.getId() not in special_products):
            total_price += p.getPrice()
    return total_price