from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':"نام خود را وارد کنید", 'class': "input-block-level"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder':"ایمیل خود را وارد کنید", 'class': "input-block-level"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': "پسوورد خود را وارد کنید", 'class': "input-block-level"}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"پسوورد خود را مجدد وارد کنید", 'class': "input-block-level"}))