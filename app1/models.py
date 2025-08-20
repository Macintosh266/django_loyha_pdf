from django.db import models

class CarModel(models.Model):
    title=models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Cars(models.Model):
    title=models.CharField(max_length=50)
    context=models.TextField(blank=True)
    create_ed=models.DateTimeField(auto_now_add=True)
    update_ed=models.DateTimeField(auto_now_add=True)
    carmodel=models.ForeignKey(CarModel,on_delete=models.CASCADE)
    photo=models.ImageField(upload_to='photo/%Y/%m/%d/')
    is_bool=models.BooleanField(default=True)
    views=models.IntegerField(default=0)
    def __str__(self):
        return self.title

# Create your models here.
