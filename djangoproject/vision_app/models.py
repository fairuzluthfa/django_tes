from django.db import models
from django.utils.timezone import now

# Create your models here.
    
class upt_model(models.Model):
    UPT=models.CharField(max_length=100,primary_key=True)
    UPT_Koordinat=models.CharField(max_length=45, blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.UPT

class ultg_model(models.Model):
    UPT_1=models.ForeignKey(upt_model,on_delete=models.CASCADE,related_name='upt_id',null=True,blank=True)
    ULTG=models.CharField(max_length=50,primary_key=True)
    ULTG_Koordinat=models.CharField(max_length=45)
    Alamat=models.CharField(max_length=100,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ULTG

class GI_model(models.Model):
    # UPT=models.ForeignKey(upt_model,on_delete=models.CASCADE,related_name='upt_ids',null=True,blank=True)
    ULTG=models.ForeignKey(ultg_model,on_delete=models.CASCADE,related_name='ultg_id')
    GIS=models.CharField(max_length=50,primary_key=True)
    GPS_Koordinat=models.CharField(max_length=45)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):  
        return f'{self.GIS}--{self.ULTG.ULTG}'
    
class nodes_model(models.Model):
    GIS=models.ForeignKey(GI_model,on_delete=models.CASCADE,related_name='GI_tes',null=True)
    node_id=models.CharField(max_length=45,unique=True,primary_key=True)
    GPS_Koordinat=models.CharField(max_length=45)
    Merk=models.CharField(max_length=45,null=True,blank=True)
    type=models.CharField(max_length=45,null=True,blank=True)
    zona_instalasi=models.CharField(max_length=10,null=True,blank=True)
    isolasi=models.CharField(max_length=10,null=True,blank=True)
    min_scale=models.FloatField(null=True,blank=True)
    max_scale=models.FloatField(null=True,blank=True)
    min_value=models.IntegerField(null=True,blank=True)
    max_value=models.IntegerField(null=True,blank=True)
    Date_time=models.DateTimeField(auto_now_add=True)
    IP=models.CharField(max_length=45,null=True,blank=True)

    def __str__(self):
        return self.node_id

    
class realtimes_model(models.Model):
    node=models.ForeignKey(nodes_model,on_delete=models.CASCADE,related_name='realtimes_data')
    acquired_at=models.DateTimeField(blank=True,null=True)
    Pressure=models.FloatField()
    Temperature=models.FloatField()
    Humidity=models.FloatField()

    Status_cam=models.CharField(default='on',max_length=45)
    Status_gauge=models.CharField(default='aman',max_length=45)
    File_image=models.ImageField(upload_to='vision/',null=True, blank=True)

    def __str__(self):    
        return f'{self.node.node_id}--{self.acquired_at}'
    
class user_model(models.Model):
    user_id=models.CharField(max_length=100,primary_key=True)
    user_name=models.CharField(max_length=100,null=False,blank=False)
    password=models.CharField(max_length=20,null=True,blank=True)
    nama=models.CharField(max_length=100,null=True,blank=True)
    alamat=models.CharField(max_length=100,null=True,blank=True)
    no_hp=models.CharField(max_length=20,default='0',null=True,blank=True)
    unit=models.ManyToManyField(GI_model)

    def __str__(self):
        return f'{self.user_id}--{self.user_name}'

class image_model(models.Model):
    node=models.ForeignKey(nodes_model, on_delete=models.CASCADE,related_name='images_data')
    photo=models.ImageField(upload_to='vision/')
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.node.node_id}--{self.photo}--{self.uploaded_at.strftime(rf'%d-%m-%y %H:%M')}'
    


   