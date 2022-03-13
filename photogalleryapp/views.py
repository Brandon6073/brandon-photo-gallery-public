from django.shortcuts import render, redirect
from .models import Category, Photo

from django.contrib.auth import authenticate,login,logout

from django.contrib import messages #flash message

from django.contrib.auth.decorators import login_required # decorator for restricted access

from .decorators import allowed_users



def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password = password)

        if request.user.is_authenticated:
            messages.info(request,'Admin is already logged in')
        elif user is not None:
            login(request,user)
            return redirect('gallery')
        else:
            messages.info(request, 'Username or password is incorrect')
    context = {}

    return render(request, 'photogalleryapp/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('gallery')

def gallery(request):
    category = request.GET.get('category')
    # filter by category

    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name =category)
        
    categories = Category.objects.all()

    context = {'categories':categories, 'photos':photos}

    return render(request,'photogalleryapp/gallery.html', context)
    

def photoView(request,pk):
    photo = Photo.objects.get(id=pk)

    context = {'photo': photo}

    return render(request,'photogalleryapp/photo_view.html',context)


def photoAdd(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
            # if category is not 'none'

        elif data['category_add'] != '':
            category,created = Category.objects.get_or_create(name = data['category_add'])
            # if the user add new category
            # get existing or create new one

        else:
            category = None
            # category can be set to none

        
        photo = Photo.objects.create(
            category = category, # category choosen (from db, choosen or none)
            description = data['description'],
            image=image,
        )

        return redirect('/')
    context = {'categories':categories}
    return render(request,'photogalleryapp/photo_add.html',context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def photoUpdate(request,pk):

    categories = Category.objects.all()
    photo = Photo.objects.get(id=pk)

    if request.method == "POST":
        data = request.POST

        if len(request.FILES) != 0:
            # if the user add a new image file 
            old_image = photo.image # the image before update

            image = request.FILES.get('image') # the image after update

            old_image.delete()            
    
        else:
            image = photo.image
            # image with space cant load

        if data['category_add'] != '':
            category,created = Category.objects.get_or_create(name = data['category_add'])

        elif data['category'] != 'none':
            category = Category.objects.get(id=data['category'])

        else:
            category = None


        # updatePhoto = Photo.objects.filter(id=pk).update (
        # category = category, # category choosen (from db, choosen or none)
        # description = data['description'],
        # image=image,
        # )
        # print('image last:',updatePhoto)

        photo.category = category
        # photo.description = data.get('description')
        photo.description = data['description']
        photo.image = image

        photo.save()
        
        return redirect('/')

    context = {'photo': photo, 'categories':categories}
    return render(request,'photogalleryapp/photo_update.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def photoDelete(request,pk):

    photo = Photo.objects.get(id=pk)

    # if confirmed
    if request.method == "POST":
        photo.image.delete()
        photo.delete()
        print("photo status:",photo)

        return redirect('/')

    
    context = {'photo':photo}
    return render(request, 'photogalleryapp/photo_delete.html', context)