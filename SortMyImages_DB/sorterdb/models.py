from django.db import models

# Create your models here.
class ImagesTraining(models.Model):
    img=models.FileField(upload_to='images-training')
    id=models.AutoField(primary_key=True,auto_created=True)

class ImagesUnuseable(models.Model):
    img=models.FileField(upload_to='images-unuseable')
    id=models.AutoField(primary_key=True,auto_created=True)
