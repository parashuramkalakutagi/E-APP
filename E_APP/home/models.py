from django.db import models


import uuid
from accounts.models import Profile
from datetime import timedelta
from django.utils import timezone
import datetime

class BaseModel(models.Model):
    uuid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract  = True


class Brand(models.Model):
    brand_name = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name
class Catagory(models.Model):
    catagory = models.CharField(max_length=100)

    def __str__(self):
        return self.catagory
class Colour(models.Model):
    colour = models.CharField(max_length=100)

    def __str__(self):
        return self.colour
class Mobile(BaseModel):
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    catagory = models.ForeignKey(Catagory,on_delete=models.CASCADE)
    name =  models.CharField(max_length=100)
    discription = models.TextField()
    image = models.FileField(upload_to='mobiles/')
    colour = models.ForeignKey(Colour,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    price_off = models.FloatField(default=0,null=True,blank=True)
    storage = models.CharField(max_length=100)
    popularity = models.IntegerField(default=0,null=True,blank=True)
    rating = models.IntegerField(default=0,null=True,blank=True)

    def __str__(self):
        return f'{str(self.brand)} uuid >>  {str(self.uuid)}'
class Highlights(BaseModel):
    mobile = models.ForeignKey(Mobile,on_delete=models.CASCADE,related_name='highlights',related_query_name='highlights')
    ram = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    camera = models.CharField(max_length=100)
    front_camera = models.CharField(max_length=100)
    display = models.CharField(max_length=100)
    battery = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.mobile}______Hg_uuid____{self.uuid}'
    
class Others_Details(BaseModel):
    mobile = models.ForeignKey(Mobile,on_delete=models.CASCADE,related_name='other_details',related_query_name='other_details')
    network =models.CharField(max_length=100)
    sim_type = models.CharField(max_length=100)
    expandible_storage = models.CharField(max_length=100)
    audio_jack = models.CharField(max_length=100)
    quick_charge = models.CharField(max_length=100)
    in_the_box = models.CharField(max_length=100)
    warranty = models.CharField(max_length=100)

    def __str__(self):
        return str(self.mobile)

class Laptops(BaseModel):
    brand_name = models.CharField(max_length=3000)
    price = models.CharField(max_length=100)
    discription = models.TextField()
    reviews = models.CharField(max_length=100)

    def __str__(self):
        return self.brand_name
