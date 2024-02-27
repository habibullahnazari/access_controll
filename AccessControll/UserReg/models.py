from django.db import models

# Create your models here.


class RegisterU(models.Model):
    EmID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    photo = models.ImageField(
        upload_to='media/emphoto', height_field=None, width_field=None)
    allowed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
