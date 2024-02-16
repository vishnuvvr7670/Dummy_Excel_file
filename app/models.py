from django.db import models

# Create your models here.
class Business(models.Model):
    series_reference=models.CharField(max_length=100)
    series_num=models.DecimalField(max_digits=10,decimal_places=2)
    data_value=models.DecimalField(max_digits=10,decimal_places=10,null=True,blank=True)
    supressed=models.CharField(max_length=100,null=True,blank=True)
    status=models.CharField(max_length=100)
    units=models.CharField(max_length=100)
    magnitude=models.IntegerField()
    subject=models.CharField(max_length=200)
    group=models.CharField(max_length=100)
    series_title1=models.CharField(max_length=100)
    series_title2=models.CharField(max_length=100)
    series_title3=models.CharField(max_length=100)

    def __self__(self):
        return self.series_reference