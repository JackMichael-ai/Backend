# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from Admin.models import Item


def dashboard(request):
    items = Item.objects.all()
    return render(request, 'dashboard.html', {'items': items})


def add_item(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')
        # CRITICAL: Get the image from request.FILES


        Item.objects.create(
            image=image,
            title=title,
            description=description,
            category=category,
            price=price,

        )
        return redirect('dashboard')
    return render(request, 'add_item.html')


def update_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        if request.FILES.get('image'):
            item.image = request.FILES.get('image')
        item.title = request.POST.get('title')
        item.description = request.POST.get('description')
        item.category = request.POST.get('category')
        item.price = request.POST.get('price')

        # Handle image update if a new one is uploaded
        if request.FILES.get('image'):
            item.image = request.FILES.get('image')

        item.save()
        return redirect('dashboard')
    return render(request, 'Update_item.html', {'item': item})