from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from wfutureAPI.templatetags.user_type_tags import is_volunteer
from wfutureAPI.models.transaction import Transaction
from wfutureAPI.models.storeitem import StoreItem
from .cart import Cart
from .forms import CartAddStoreItemForm
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

@require_POST
@user_passes_test(is_volunteer)
def cart_add(request, storeitem_id):
    cart = Cart(request)
    storeitem = get_object_or_404(StoreItem, id=storeitem_id)
    form = CartAddStoreItemForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        total_cost = storeitem.points_cost * cd['quantity']
        
        # Check if user has enough points
        volunteer = request.user.volunteer
        if total_cost <= volunteer.points:
            cart.add(storeitem=storeitem,
                     quantity=cd['quantity'],
                     update_quantity=cd['update'])
        else:
            messages.error(request, "You do not have enough points.")
    return redirect('cart:cart_detail')

@user_passes_test(is_volunteer)
def cart_remove(request, storeitem_id):
    cart = Cart(request)
    storeitem = get_object_or_404(StoreItem, id=storeitem_id)
    cart.remove(storeitem)
    return redirect('cart:cart_detail')

@user_passes_test(is_volunteer)
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddStoreItemForm(initial={'quantity': item['quantity'],
                                                                     'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})

@user_passes_test(is_volunteer)
def submit_order(request):
    cart = Cart(request)
    volunteer = request.user.volunteer
    total_price = cart.get_total_price()
    
    if total_price <= volunteer.points:
        for item in cart:
            Transaction.objects.create(
                volunteer=request.user,
                storeitem=item['storeitem'],
                quantity=item['quantity'],
                total_points=item['total_price']
            )
        
        # Deduct points
        volunteer.points -= total_price
        volunteer.save()
        
        # Clear the cart
        cart.clear()
        
        messages.success(request, "Order submitted successfully!")
        return redirect('cart:cart_detail')
    else:
        messages.error(request, "You do not have enough points to submit the order.")
        return redirect('cart:cart_detail')
    
def transaction_history(request):
    transactions = Transaction.objects.filter(volunteer=request.user).order_by('-date')
    return render(request, 'cart/transaction_history.html', {'transactions': transactions})

