from django.shortcuts import render, redirect, get_object_or_404

from Admin.models import Item


# Create your views here.
def dashboard(request):
    items = Item.objects.all()
    return render(request, 'dashboard.html' , {'items': items})

def add_item(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')
        Item.objects.create(
            title=title,
            description=description,
            category=category,
            price=price
        )
        return redirect('dashboard')
    return render(request, 'add_item.html')

def update_item(request,id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.title = request.POST.get('title')
        item.description = request.POST.get('description')
        item.category = request.POST.get('category')
        item.price = request.POST.get('price')
        item.date = request.POST.get('date')
        item.save()
        return redirect('dashboard')
    return render(request, 'Update_item.html' ,{'item': item})
