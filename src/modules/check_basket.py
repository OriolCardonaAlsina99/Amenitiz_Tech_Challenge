def handle_basket (products, total_price):
    for p in products:
        if (p.getId() != 'GR1' and p.getId() != 'SR1' and p.getId() != 'CF1'):
            total_price += p.getPrice()
    return total_price