from cProfile import label
# from xml.dom.xmlbuilder import Options
from django import forms
from .models import *

# creating a drop down for category
# CATEGORY_CHOICE=(
#     ('fashion','Fashion'),
#     ('wildlife','Wildlife'),
#     ('sport','Sports'),
#     ('car','Cars'),
#     ('nature','Nature'),
# )

# # creating a list for locations
# LOCATION_CHOICE=(
#      ('nairobi','Nairobi'),
#     ('nakuru','Nakuru'),
#     ('mombasa','Mombasa'),
#      ('kisumu','Kisumu'),
# )
#creating forms for models 
class ImageForm(forms.ModelForm):
   
    class  Meta:
       model = Image 
       fields = ('image','image_name','image_description','location','category')
       
class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields= ('location',)
        templates = ('photo/imageform')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields= ('category',)
        templates = ('photo/imageform')       
        
        
        
        