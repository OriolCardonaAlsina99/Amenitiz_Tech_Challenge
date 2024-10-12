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
        return round(final_price, 2)