from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:storeitem_id>/',
         views.cart_add,
         name='cart_add'),
    path('remove/<int:storeitem_id>/',
         views.cart_remove,
         name='cart_remove'),
    path('submit/', views.submit_order, name='submit_order'),
    path('history/', views.transaction_history, name='transaction_history'),
]