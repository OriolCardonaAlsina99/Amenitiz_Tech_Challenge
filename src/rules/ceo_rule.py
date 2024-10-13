def CEO_rule (products):
    price = 0
    for p in products:
        price += p.getPrice()
    size_arr = len(products)
    if (size_arr < 2):
        return price
    if (size_arr%2 == 0):
        return price/2
    else:
        green_tea_price = products[0].getPrice()
        size_arr = len(products) - 1
        final_price = ((green_tea_price*size_arr)/2 + green_tea_price)
        return round(final_price, 2)