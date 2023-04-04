from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    author =models.CharField(max_length=50)
    desc = models.CharField(max_length=4000)
    img = models.ImageField( upload_to='images/', height_field=None, width_field=None, max_length=None)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.title