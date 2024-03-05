from django.db import models

class Imagemodel(models.Model):
    date=models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to='my_images')
