from modules.ceo_rule import CEO_rule
from modules.coo_rule import COO_rule
from modules.vp_rule import VP_rule

def handle_rules(products):
    green_teas = []
    strawberries = []
    coffies = []
    for p in products:
        if (p.getId() == 'GR1'):
            green_teas.append(p)
        if (p.getId() == 'SR1'):
            strawberries.append(p)
        if (p.getId() == 'CF1'):
            coffies.append(p)
    total_price = CEO_rule(green_teas) + COO_rule(strawberries) + VP_rule(coffies)
    return total_price