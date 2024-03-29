from django.shortcuts import render, redirect
from .models import Category, Photo
from django.contrib.auth.decorators import login_required

@login_required
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = { 'categories' : categories, 'photos': photos }
    return render(request, 'gallery.html', context)

@login_required
def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    context = { 'photo': photo }
    return render(request, 'photo.html', context)

@login_required
def addPhoto(request):
    categories = Category.objects.all()
    context = { 'categories' : categories }

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        
        print(data)
        if data['category'] != 'none':
            category  = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image
        )
        return redirect('gallery')
    
    return render(request, 'add.html', context)
