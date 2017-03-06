from django import forms
from CatoApp.models import *
from django.contrib.admin.widgets import AdminDateWidget


class SearchForm(forms.Form):
    education = forms.ChoiceField(choices=EDUCATION_CHOICES, widget=forms.RadioSelect, required=False)
    major = forms.ChoiceField(choices=MAJOR_CHOICES, widget=forms.RadioSelect, required=False)
    zipcode = forms.IntegerField(max_value=99999, min_value=0, required=False)

    def matched_jobs(self):
        # job search logic goes here
        return [] #job found goes here


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput,max_length=16,min_length=6)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        if not User.objects.filter(email=email, password=password).values('id').first():
            raise forms.ValidationError("Authentication failed")
        return cleaned_data

    def login(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        return User.objects.get(email=email, password=password).id


class SignUpForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(max_length=16,min_length=6,widget=forms.PasswordInput)
    confirm_pw = forms.CharField(max_length=16,min_length=6,widget=forms.PasswordInput)
    education = forms.ChoiceField(choices=EDUCATION_CHOICES,widget=forms.RadioSelect,required=False)
    graduation_date = forms.DateField(required=False,widget=forms.SelectDateWidget)
    major = forms.ChoiceField(choices=MAJOR_CHOICES,widget=forms.RadioSelect,required=False)
    zipcode = forms.IntegerField(max_value=99999,min_value=0,required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean_confirm_pw(self):
        confirm_pw = self.cleaned_data['confirm_pw']
        if self.cleaned_data['password'] != confirm_pw:
            raise forms.ValidationError("Passwords do not match")
        return confirm_pw

    # def clean(self):
    #     cleaned_data = super(LoginForm, self).clean()
    #     email = cleaned_data.get('email')
    #     password = cleaned_data.get('password')
    #     confirm_pw = cleaned_data.get('confirm_pw')
    #     education = cleaned_data.get('education')
    #     graduation_date = cleaned_data.get('graduation_date')
    #     major = cleaned_data.get('major')
    #     zipcode = cleaned_data.get('zipcode')
    #     return cleaned_data

    def sign_up(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        education = self.cleaned_data.get('education')
        graduation_date = self.cleaned_data.get('graduation_date')
        major = self.cleaned_data.get('major')
        zipcode = self.cleaned_data.get('zipcode')
        new_user = User(
            email=email,
            password=password,
            education=education,
            graduation_date=graduation_date,
            major=major,
            zipcode=zipcode,
        )
        new_user.save()
        return User.objects.get(email=email, password=password).id