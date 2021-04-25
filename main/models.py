from django.db import models


# Create your models here.


class Check(models.Model):
    CHECKCATEGORY = (
        ('Storage', 'Storage'),
        ('Backup', 'Backup'),
    )

    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    category = models.CharField(max_length=200, null=True, choices=CHECKCATEGORY)
    failure_details = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.name


class Incident(models.Model):
    INCSTATE = (
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
    )
    name = models.CharField(max_length=200, null=True)
    number = models.CharField(max_length=200, null=True)
    linked_check = models.CharField(max_length=200, null=True)
    date_raised = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=INCSTATE)
    details = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class ItemState(models.Model):
    ITEMSTATE = (
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
    )
    name = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, null=True, choices=ITEMSTATE)
    note = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name
