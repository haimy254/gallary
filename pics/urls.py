from django import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('image/', image_view, name = 'index'),
	path('imageform/', image_view, name = 'imageform'),
	# path("search/",views.search_result, name="search_results"),
    path('success', success, name = 'success'),
]

if settings.DEBUG:
		urlpatterns += static(settings.MEDIA_URL,
		document_root=settings.MEDIA_ROOT)
