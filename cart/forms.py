from django import forms


STORE_ITEM_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddStoreItemForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=STORE_ITEM_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)