from django.db import models


# Create your models here.
class SampleModel(models.Model):
    def __str__(self):
        return self.field_one
    field_one = models.CharField(max_length=200)
    field_two = models.FloatField()
    field_three = models.DateField()

class BudgetCategory(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=200)
