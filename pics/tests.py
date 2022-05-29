from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class LocationTestClass(TestCase):
    #set up method 
    def setUp(self):
        self.nairobi= Location(location='nairobi')
        
    pass