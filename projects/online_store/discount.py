from occasions import occasions
class Discounts:
    def __init__(self,cart,occasian):
        if not isinstance(occasian,occasions):
            raise ValueError(f'no such occasion')
        for i in cart.cart:
            cart.cart[i]['price'] -= (cart.cart[i]['price'] * (occasian.discount / 100.0))
        print('discount succecfuly has been done')