from django.db import models

# Create your models here.
class ToDotb(models.Model):
    task=models.CharField(max_length=30)
    priority=models.IntegerField()
    date=models.DateField()
    def __str__(self):
        return self.task
