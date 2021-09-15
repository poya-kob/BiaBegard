from django import forms


class UserNewOrderForm(forms.Form):
    product_id = forms.IntegerField(

        widget=forms.HiddenInput()

    )

    count = forms.IntegerField(

        widget=forms.NumberInput(attrs={'type': "text", 'name': "num", 'value': "1", 'class': "tiny-size"}),
        initial=1

    )
