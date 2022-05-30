from cProfile import label
# from xml.dom.xmlbuilder import Options
from django import forms
from .models import *


# #creating forms for models 
class SearchForm(forms.ModelForm):
   
    class  Meta:
       model = Image 
       fields = ('image','image_name','image_description','location','category')
       
# class LocationForm(forms.ModelForm):
#     class Meta:
#         model = Location
#         fields= ('location',)
#         templates = ('photo/imageform')

# class CategoryForm(forms.ModelForm):
#     class Meta:
#         model = Category
#         fields= ('category',)
#         templates = ('photo/imageform')       
        
        
        
        