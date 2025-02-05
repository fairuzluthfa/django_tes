from django.db import models

# Create your models here.

class Device(models.Model):
    device_id=models.CharField(max_length=100,unique=True)
    name=models.CharField(max_length=100)
    status=models.BooleanField(default=True)
    last_seen=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class SensorData(models.Model):
    device=models.ForeignKey(Device,on_delete=models.CASCADE,related_name='sensor_data1')
    temperature=models.FloatField()
    humidity=models.FloatField()
    timestamp=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.device}  {self.timestamp}'

    # class Meta:
    #     ordering=[-time]


