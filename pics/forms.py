from cProfile import label
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
class ImageForm(forms.ModelForm):
    class  Meta:
       model = Image 
       fields = ['image','image_name','image_description','location','category']
    # image = forms.ImageField(label='upload image')
    # image_names= forms.CharField(label = 'image name')
    # image_description=forms.CharField(label='description of the image')
    # location = forms.CharField(label='select image location',widget=forms.Select(choices=LOCATION_CHOICE))
    # category = forms.CharField(label='select image category',widget=forms.Select(choices=CATEGORY_CHOICE))
        
        
        
        
        
        