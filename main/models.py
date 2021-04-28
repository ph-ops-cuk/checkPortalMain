from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Incident(models.Model):
    name = models.CharField(max_length=200, null=True, default='null')

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=200, null=True)
    user_id = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Site(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Check(models.Model):
    FREQUENCY = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
    )
    AUTO = (
        ('Manual', 'Manual'),
        ('Email', 'Email'),
        ('Automated', 'Automated'),
    )
    name = models.CharField(max_length=200, null=True)
    check_frequency = models.CharField(max_length=200, null=True, choices=FREQUENCY, default='Daily')
    check_automation = models.CharField(max_length=200, null=True, choices=AUTO, default='Manual')
    category_id = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    site_id = models.ForeignKey(Site, null=True, on_delete=models.SET_NULL)
    team_id = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    tag_id = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Result(models.Model):
    RESULTSTATE = (
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
    )
    check_id = models.ForeignKey(Check, null=True, on_delete=models.SET_NULL)
    incident_id = models.ForeignKey(Incident, null=True, on_delete=models.SET_NULL)
    category_id = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    site_id = models.ForeignKey(Site, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=RESULTSTATE)
    notes = models.CharField(max_length=500, null=True, default='null')
    date_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.status


class ResMapping(models.Model):
    result_id = models.ForeignKey(Result, null=True, on_delete=models.SET_NULL)
    incident_id = models.ForeignKey(Incident, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.incident_id
