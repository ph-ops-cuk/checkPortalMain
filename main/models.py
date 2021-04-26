from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Check(models.Model):
    name = models.CharField(max_length=200, null=True)
    category_id = models.ForeignKey(Category, null=True, on_delete= models.SET_NULL)
    tag_id = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name


class Result(models.Model):
    RESULTSTATE = (
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
    )
    check_id = models.ForeignKey(Check, null=True, on_delete= models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=RESULTSTATE)
    date_time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.status
