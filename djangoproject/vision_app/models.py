from django.db import models

# Create your models here.

class nodes_model(models.Model):
    node_id=models.CharField(max_length=45,unique=True)
    GPS_Koordinat=models.CharField(max_length=45)
    Merk=models.CharField(max_length=45,default=None)
    type=models.CharField(max_length=45,default=None)
    zona_instalasi=models.CharField(max_length=10,default=None)
    isolasi=models.CharField(max_length=10,default=None)
    # min_scale=models.FloatField()
    # max_scale=models.FloatField()
    # min_value=models.IntegerField()
    # max_value=models.IntegerField()
    Date_time=models.DateTimeField(auto_now_add=True)
    # IP

    def __str__(self):
        return self.node_id
    

class realtimes_model(models.Model):
    node=models.ForeignKey(nodes_model,on_delete=models.CASCADE,related_name='realtimes_data')
    Date_time=models.DateTimeField(auto_now_add=True)
    Pressure=models.FloatField()
    Status_cam=models.CharField(default='on',max_length=45)
    Status_gauge=models.CharField(default='aman',max_length=45)
    File_image=models.CharField(max_length=100)

    def __str__(self):
        return f'{self.node.node_id}--{self.Date_time}'
