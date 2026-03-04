print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print("I AM THE REAL VIEWS FILE")
print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages, auth
from Admin.models import Item


# --- AUTH VIEWS ---

def signup(request):
    if request.method == 'POST':
        u_name = request.POST.get('username')
        email = request.POST.get('email')
        p_word = request.POST.get('password')

        if User.objects.filter(username=u_name).exists():
            messages.error(request, 'Username taken.')
            return render(request, 'signup.html', {'last_username': u_name})

        user = User.objects.create_user(username=u_name, email=email, password=p_word)
        auth.login(request, user)
        messages.success(request, f"Welcome, {u_name}!")
        return redirect('dashboard')

    return render(request, 'signup.html')


def login(request):
    # 1. Protection Pattern: Don't show login if already logged in
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')

        user = auth.authenticate(username=u_name, password=p_word)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            # 2. Direct Injection: Bypassing potential Middleware issues
            return render(request, 'login.html', {
                'error_manual': "Invalid username or password.",
                'last_username': u_name
            })

    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('login')


# --- CORE APP VIEWS ---

@login_required
def dashboard(request):
    items = Item.objects.all().order_by('-id')  # Pattern: Newest items first
    return render(request, 'dashboard.html', {'items': items})


@login_required
def add_item(request):
    if request.method == 'POST':
        # Quick Grab Pattern
        Item.objects.create(
            image=request.FILES.get('image'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=request.POST.get('category'),
            price=request.POST.get('price')
        )
        messages.success(request, "Item added successfully!")
        return redirect('dashboard')
    return render(request, 'add_item.html')


@login_required
def update_item(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == 'POST':
        # Update only if data is provided (Literal Logic)
        item.title = request.POST.get('title') or item.title
        item.description = request.POST.get('description') or item.description
        item.category = request.POST.get('category') or item.category
        item.price = request.POST.get('price') or item.price

        if request.FILES.get('image'):
            item.image = request.FILES.get('image')

        item.save()
        messages.success(request, f"'{item.title}' updated!")
        return redirect('dashboard')

    return render(request, 'Update_item.html', {'item': item})


@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        messages.warning(request, "Item deleted.")
    return redirect('dashboard')