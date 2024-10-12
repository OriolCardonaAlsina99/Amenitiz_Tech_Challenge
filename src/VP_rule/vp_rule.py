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
        return round(final_price, 2)