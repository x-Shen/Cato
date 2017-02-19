from django.db import models

# Note for teammates:
# Django automatically add an ID AutoField for models that do not have a primary key specified


class User(models.Model):
    email = models.CharField(max_length=256)
    password = models.CharField(max_length=16)
    education = models.CharField(max_length=16)


class Skill(models.Model):
    name = models.CharField(max_length=32)


class Job(models.Model):
    title = models.CharField(max_length=256)
    company = models.CharField(max_length=256)
    last_updated = models.DateField(auto_now_add=True)
    posting_date = models.DateField(null=True)


class UserHasSkill(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)


class JobNeedSkill(models.Model):
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill,on_delete=models.CASCADE)


class UserSeenJob(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    starred = models.BooleanField()
    dismissed = models.BooleanField()
    viewed_count = models.PositiveIntegerField()