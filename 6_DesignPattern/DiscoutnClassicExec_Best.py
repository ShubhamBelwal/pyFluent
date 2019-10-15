from DiscountFunction import Customer,LineItem,Order,bulk_item_promo,large_order_promo,fidelity_promo
import inspect
import promotions

# Version 1
# promos = [fidelity_promo,bulk_item_promo,large_order_promo]

# Version 2
# promos = [globals()[name] for name in globals()
#             if name.endswith('_promo')
#             and name != 'best_promo']

# Version 3
promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]
def best_promo(order):
    """Select best available discount"""
    return max(promo(order) for promo in promos)

joe = Customer('John Doe', 0)
ann = Customer('Lisa Anne', 1100)
cart = [LineItem('banana', 4, .5),
        LineItem('apple', 10, 1.5),
        LineItem('watermelon', 5, 5.0)]
banana_cart = [LineItem('banana', 30, .5),
               LineItem('apple', 10, 1.5)]
long_order = [LineItem(str(item_code), 1, 1.0)
              for item_code in range(10)]

print(Order(joe, long_order, best_promo))
print(Order(joe, banana_cart, best_promo))
print(Order(ann, cart, best_promo))