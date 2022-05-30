from ast import Try
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .models import Image

# Create your views here.
def image_view(request):

	if request.method == 'POST':
		form = Image(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = Image()
	return render(request, 'photo/imageform.html', {'form' : form})


def success(request):
	return HttpResponse('successfully uploaded')

def display_images(request):
    if request.method=="GET":
        images=Image.objects.all();
        return render(request,'show_images.html',{'all_images':images})
    
def home_view(request):
    return render(request,'home.html')

def get_update(request,image_id):
    the_id=int(image_id)
    
    try:
        image_sel=Image.objects.get(id=the_id)
        return render(request,'update_form.html',{'selected_image':image_sel})
    except:
        images=Image.objects.all()
        return render(request,'show_images.html',{'all_images':images})
    
def post_update(request,image_id):
    image_id= int(image_id)
    
    try:
        image_sel=Image.objects.post(id =image_id)
        image=Image(request.POST or None, instance=image_sel)
        if image.is_valid():
            image.save()
        return redirect('show_images.html',{'all_images':image})
    except Image.DoesNotExist:
        images=Image.objects.all()
        return redirect ('show_images.html',{'all_images':images})
    
def display_details(request,image_id):
    the_image_id=int(image_id)
    
    try:
        image_sel=Image.objects.get(id =the_image_id)
        return redirect('details.html',{'selected_image':image_sel})
    except Image.DoesNotExist:
        images=Image.objects.all()
        return redirect ('show_images.html',{'all_images':images})
   
    
    
def delete_image(request,image_id):
    the_id=int(image_id)
    images=0

    try:
        image_sel=Image.objects.get(id=the_id)
        image_sel.delete()
        images=Image.objects.all()
        return render(request,'show_images.html',{'all_images':images})
    except:
        images=Image.objects.all()
        return render(request,'show_images.html',{'all_images':images})
    
    #search function to post the category
@csrf_exempt
def search(request):   
    if request.method=='POST':
        search_term = request.POST.get("category",False)
        print(search_term)
        category=Image.search_by_category(search_term)
        if category is None:
            HttpResponse('theres not such a category')
        else:
            searched_images = Image.search_by_category(search_term)
            print(searched_images)
            message = f"{search_term}"   
            return render(request, 'search.html',{"message":message,"images": searched_images})   
    else:
         message = "You haven't searched for any image"
    return render(request, 'search.html',{"message":message})
        
    

        
    