from django.conf import settings
from wfutureAPI.models.storeitem import StoreItem

class Cart(object):
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        storeitem_ids = self.cart.keys()
        storeitems = StoreItem.objects.filter(id__in=storeitem_ids)

        cart = self.cart.copy()
        for storeitem in storeitems:
            cart[str(storeitem.id)]['storeitem'] = storeitem

        for item in cart.values():
            item['points_cost'] = int(item['points_cost'])
            item['total_price'] = item['points_cost'] * item['quantity']
            yield item
    
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, storeitem, quantity=1, update_quantity=False):
        storeitem_id = str(storeitem.id)
        if storeitem_id not in self.cart:
            self.cart[storeitem_id] = {
                'quantity': 0,
                'points_cost': str(storeitem.points_cost)
            }
        if update_quantity:
            self.cart[storeitem_id]['quantity'] = quantity
        else:
            self.cart[storeitem_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def remove(self, storeitem):
        storeitem_id = str(storeitem.id)
        if storeitem_id in self.cart:
            del self.cart[storeitem_id]
            self.save()

    def get_total_price(self):
        return sum(int(item['points_cost']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.save()
