from django.shortcuts import get_object_or_404, render
from cart.forms import CartAddStoreItemForm
from django.contrib.auth.decorators import user_passes_test

from ..templatetags.user_type_tags import is_volunteer
from ..models.storeitem import StoreItem

@user_passes_test(is_volunteer)
def storeitem_list(request):
    storeitems = StoreItem.objects.filter(available=True)
    return render(request, 'storeitem/list.html',
                  {
                      'storeitems': storeitems
                  })

@user_passes_test(is_volunteer)
def storeitem_detail(request, id):
    storeitem = get_object_or_404(StoreItem, id=id, available=True)
    cart_storeitem_form = CartAddStoreItemForm()
    return render(request, 'storeitem/detail.html', {'storeitem': storeitem, 'cart_storeitem_form': cart_storeitem_form})