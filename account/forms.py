from django.forms import forms


class LoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید', 'class': 'input-block-level'})

    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمزعبور خود را وارد کنید', 'class': 'input-block-level'}),
    )
