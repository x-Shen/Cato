# from django_select2.forms import *
from django import forms
from CatoApp import models


# class SkillSelect2TagWidget(ModelSelect2TagWidget):
#     queryset = models.Skill.objects.all()
#
#     def value_from_datadict(self, data, files, name):
#         values = super().value_from_datadict(self, data, files, name)
#         qs = self.queryset.filter(**{'pk__in': list(values)})
#         pks = set(force_text(getattr(o, self.queryset.pk)) for o in qs)
#         cleaned_values = []
#         for val in values:
#             if force_text(val) not in pks:
#                 val = self.queryset.create(name=val).pk
#             cleaned_values.append(val)
#         return cleaned_values


class SearchForm(forms.Form):
    skills = forms.ModelMultipleChoiceField(
        queryset=models.Skill.objects.all().order_by('name'),
        to_field_name="name",
        required=False
    )
    education = forms.ChoiceField(choices=models.EDUCATION_CHOICES, required=False, disabled=True)
    major = forms.ChoiceField(choices=models.MAJOR_CHOICES, required=False, disabled=True)
    zipcode = forms.IntegerField(max_value=99999, min_value=0, required=False, disabled=True)

    def matched_jobs(self):
        jobs = models.Job.objects.all()
        # # how to find related skills
        # for job in jobs:
        #     skills = job.jobneedskill_set.select_related('skill')
        #     for skill in skills:
        #         print(skill.skill)
        #     print("end of job "+job.title)
        if hasattr(self, 'cleaned_data'):
            jobs = jobs.filter(jobneedskill__skill__in=self.cleaned_data.get('skills'))
            # education
            # major
            # zipcode

        # add required skill to jobs
        to_return = {}
        jobs = jobs.prefetch_related('jobneedskill_set__skill')
        for job in jobs:
            to_return[job] = job.jobneedskill_set.all()# jobs.filter(job=job).values('jobneedskill__skill')# models.Skill.objects.filter(jobneedskill__job=job)
        return to_return

        # return jobs



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput, max_length=16, min_length=6)
    user_id = None

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user_id = models.User.objects.filter(email=email, password=password).values('id').first()
        if not user_id:
            raise forms.ValidationError("Authentication failed")
        return cleaned_data

    def login(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        return models.User.objects.get(email=email, password=password).id


class SignUpForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput)
    confirm_pw = forms.CharField(max_length=16, min_length=6, widget=forms.PasswordInput)
    education = forms.ChoiceField(choices=models.EDUCATION_CHOICES, widget=forms.RadioSelect, required=False)
    graduation_date = forms.DateField(required=False, widget=forms.SelectDateWidget)
    major = forms.ChoiceField(choices=models.MAJOR_CHOICES, widget=forms.RadioSelect, required=False)
    zipcode = forms.IntegerField(max_value=99999, min_value=0, required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if models.User.objects.filter(email=email).exists():
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
        new_user = models.User(
            email=email,
            password=password,
            education=education,
            graduation_date=graduation_date,
            major=major,
            zipcode=zipcode,
        )
        new_user.save()
        return models.User.objects.get(email=email, password=password).id
