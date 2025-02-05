from django.db import models
import uuid

# Create your models here.
class realtime_data(models.Model):
    Node_ID=models.CharField(max_length=50,unique=False,null=False)
    Date=models.DateField(auto_now_add=True)
    Time=models.TimeField(auto_now_add=True)
    Pressure=models.FloatField()
    Status_Cam=models.BooleanField(default=True)
    Status_Normal=models.BooleanField(default=True)
    File_image=models.CharField(max_length=500)
    id=models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.Node_ID)+str(self.Date)
