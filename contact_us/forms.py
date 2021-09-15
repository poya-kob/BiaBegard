from django import forms
from django.core import validators


class CreateContactForm(forms.Form):
    full_name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'نام  و نام خانوادگی خود را وارد کنید', 'class': 'input-block-level'}),
        label="نام و نام خانوادگی",
        validators=[
            validators.MaxLengthValidator(200, "نام و نام خانوادگی شما نمیتواند بیش از ۲۰۰ کاراکتر باشد")])

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'ایمیل خود را وارد کنید', 'class': 'input-block-level'}),
        label="ایمیل",
        validators=[
            validators.MaxLengthValidator(200, "تعداد کاراکترهایایمیل شما نمیتواند بیش از ۲۰۰ کاراکتر باشد.")
        ])

    subject = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'عنوان پیام خود را وارد کنید', 'class': 'input-block-level'}),
        label="عنوان",
        validators=[
            validators.MaxLengthValidator(200, "تعداد کاراکترهای  شما نمیتواند بیش از ۲۰۰ کاراکتر باشد.")
        ])

    text = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'متن پیام خود را وارد کنید', 'class': 'input-block-level', 'row': 7, 'cols': 70}),
        label="متن پیام",
    )
