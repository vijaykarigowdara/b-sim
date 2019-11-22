from django.db import models

# Create your models here.

class InitialParameter(models.Model):
    name = models.CharField(max_length=100,blank=False)
    unit = models.CharField(max_length=100,blank=False)
    fy_0 = models.IntegerField()
    fy_1 = models.IntegerField()
    fy_2 = models.IntegerField()
    fy_3 = models.IntegerField()
    fy_combined = models.IntegerField()

    class Meta:
        abstract = True

class SuccessFactor(InitialParameter):
    pass


class PerformanceIndicator(InitialParameter):
    pass

