from django.db import models
# Creating models
class trafficAtA(models.Model):
    Trafficdensity=models.FloatField()
    time=models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.Trafficdensity,self.time
class trafficAtB(models.Model):
    Trafficdensity = models.FloatField()
    time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.Trafficdensity,self.time
class trafficAtC(models.Model):
    Trafficdensity = models.FloatField()
    time = models.TimeField(auto_now_add=True)
    def __str__(self):
        return self.Trafficdensity,self.time
class trafficAtD(models.Model):
    Trafficdensity = models.FloatField()
    time = models.TimeField(auto_now_add=True,)
    def __str__(self):
        return self.Trafficdensity,self.time
class SignalA(models.Model):
    Signal=models.CharField(max_length=1)
    time=models.TimeField(auto_now_add=True)
class SignalB(models.Model):
    Signal=models.CharField(max_length=1)
    time=models.TimeField(auto_now_add=True)
class SignalC(models.Model):
    Signal=models.CharField(max_length=1)
    time=models.TimeField(auto_now_add=True)
class SignalDs(models.Model):
    Signal=models.CharField(max_length=1)
    time=models.TimeField(auto_now_add=True)



