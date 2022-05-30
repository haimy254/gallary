from django import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path("",home_view,name='home'),
	path("search/",search, name="search"),
    path('show_images/',display_images,name='all_images'),
    path('details/pics/<int:image_id>',display_details,name='details'),
    path('get_update/<int:image_id>',get_update,name='get_update'),
    path('delete_image/<int:image_id>',delete_image,name='delete_image'),
    # path('copy/',display_copy,name='copylink'),
    
]

if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)
