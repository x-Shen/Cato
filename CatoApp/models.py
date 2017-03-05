from django.db import models
from django.forms import ModelForm


# education options
HIGH_SCHOOL = 'HI'
UNDERGRADUATE = 'UG'
BACHELOR = 'BC'
GRADUATE = 'GD'
MASTER = 'MA'
PHD = 'PD'
DOCTOR = 'DC'
EDUCATION_CHOICES = (
    (HIGH_SCHOOL, 'High school'),
    (UNDERGRADUATE, 'Undergraduate student'),
    (BACHELOR, 'Bachelor'),
    (GRADUATE, 'Graduate student'),
    (MASTER, 'Master'),
    (PHD, 'PHD student'),
    (DOCTOR, 'Doctor'),
)
# end education

# major options
COMPUTER_SCIENCE = 'CS'
SOFTWARE_ENGINEERING = 'SE'
COMPUTER_ENGINEERING = 'CE'
COMPUTER_SCIENCE_AND_ENGINEERING = 'CA'
OTHER_STEM = 'OS'
NON_STEM = 'NS'
MAJOR_CHOICES = (
    (COMPUTER_SCIENCE, 'Computer Science'),
    (SOFTWARE_ENGINEERING, 'Software Engineering'),
    (COMPUTER_ENGINEERING, 'Computer Engineering'),
    (COMPUTER_SCIENCE_AND_ENGINEERING, 'Computer Science and Engineering'),
    (OTHER_STEM, 'Other STEM majors'),
    (NON_STEM, 'Other non-STEM majors'),
)
# end major


class User(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=16)
    # education = models.CharField(max_length=16,null=True)
    education = models.CharField(
        max_length=2,
        choices=EDUCATION_CHOICES,
        default=UNDERGRADUATE,
        null=True
    )
    graduation_date = models.DateField(null=True)
    major = models.CharField(max_length=16,null=True)
    zipcode = models.PositiveIntegerField(null=True)


class Skill(models.Model):
    name = models.CharField(max_length=32)


class Job(models.Model):
    title = models.CharField(max_length=256)
    url = models.URLField(default="")
    company = models.CharField(max_length=256)
    last_updated = models.DateField(auto_now=True)
    posting_date = models.DateField(null=True)
    valid = models.BooleanField(default=True)
    zipcode = models.PositiveIntegerField(null=True)


class UserHasSkill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)


class JobNeedSkill(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)


class UserJobRelation(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    recommended = models.BooleanField(default=False)
    starred = models.BooleanField(default=False)
    dismissed = models.BooleanField(default=False)
    viewed_count = models.PositiveIntegerField(default=0)