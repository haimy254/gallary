from sre_constants import CATEGORY
from tkinter import image_names
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
#creating forms for models 
class ImageForm(forms.ModelsForm):
    class meta:
        image = forms.ImageField(lable='upload image')
        image_names= forms.CharField(lable = 'image name')
        image_description=forms.CharField(lable='description of the image')
        category = forms.CharField(lable='select image category',widget=forms.Select(choices=CATEGORY_CHOICE))
        
        
        
        
        
        