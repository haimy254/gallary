from django import forms
from .models import *

#creating a drop down for category
CATEGORY_CHOICE=[
    ('fashion','Fashion'),
    ('wildlife','Wildlife'),
    ('sport','Sports'),
    ('car','Cars'),
    ('nature','Nature'),
]

#creating a list for locations
LOCATION_CHOICE=[
     ('nairobi','Nairobi'),
    ('nakuru','Nakuru'),
    ('mombasa','Mombasa'),
     ('kisumu','Kisumu'),
]
#creating forms for models 
class ImageForm(forms.ModelsForm):
   
    image = forms.ImageField(lable='upload image')
    image_names= forms.CharField(lable = 'image name')
    image_description=forms.CharField(lable='description of the image')
    location = forms.CharField(lable='select image location',widget=forms.Select(choices=LOCATION_CHOICE))
    category = forms.CharField(lable='select image category',widget=forms.Select(choices=CATEGORY_CHOICE))
        
        
        
        
        
        