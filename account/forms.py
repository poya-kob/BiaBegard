from django import forms


class LoginForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'نام کاربری خود را وارد کنید', 'class': 'input-block-level'})

    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'رمزعبور خود را وارد کنید', 'class': 'input-block-level'}),
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': "نام کاربری خود را وارد کنید", 'class': "input-block-level"}))
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': "ایمیل خود را وارد کنید", 'class': "input-block-level"}))
    phone = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'placeholder': "شماره تلفن خود را وارد کنید", 'type': 'tel', 'class': "input-block-level"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': "پسوورد خود را وارد کنید", 'class': "input-block-level"}))
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': "پسوورد خود را مجدد وارد کنید", 'class': "input-block-level"}))
    be_supplier = forms.BooleanField(widget=forms.CheckboxInput(attrs={'class': "checkbox"}),
                                     label="ثبت نام بعنوان فروشنده", required=False)

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError('کلمه عبور یکسان نیست')
        return password
