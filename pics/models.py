from django.db import models
from distutils.command.upload import upload

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=80)
    
    def __str__(self):
        return self.location
    
    def save_location(self):
        self.save
        
class Category(models.Model):
    category = models.CharField(max_length=80)
    
    def __str__(self):
        return self.category
    
    def save_category(self):
        self.save

class Image(models.Model):
    image = models.ImageField(upload_to='image/',default='')
    image_name = models.CharField(max_length=100)
    image_description= models.CharField(max_length=500)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    @classmethod
    def search_by_category(cls,search_term):
        image = cls.objects.filter(category__icontains=search_term)
        return image
    
    @classmethod
    def search_by_location(cls,search_term):
        image = cls.objects.filter(category__icontains=search_term)
        return image
    

    