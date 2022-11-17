from django.db import models

class groups(models.Model):
    image= models.ImageField(upload_to='pics')

