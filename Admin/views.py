# Create your views here.
from pyexpat.errors import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from Admin.models import Item
from django.contrib.auth.models import User
from django.contrib import messages, auth
@login_required
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


# --- Update Item Logic Refined ---
def update_item(request, id):
    item = get_object_or_404(Item, id=id)

    if request.method == 'POST':
        # 1. Extraction (Same as before)
        title = request.POST.get('title')
        description = request.POST.get('description')
        category = request.POST.get('category')
        price = request.POST.get('price')
        new_image = request.FILES.get('image')

        # 2. Logic Gate: Only update fields if they aren't empty
        if title: item.title = title
        if description: item.description = description
        if category: item.category = category
        if price: item.price = price

        # 3. Image Logic: Only overwrite if a new file was actually sent
        if new_image:
            item.image = new_image

        # 4. Commit to DB
        item.save()
        messages.success(request, f"Item '{item.title}' updated!")
        return redirect('dashboard')

    return render(request, 'Update_item.html', {'item': item})

def delete_item(request, id):
    item = get_object_or_404(Item, id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard')
    return redirect('dashboard')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # 1. Validation Logic
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username taken.')
            return redirect('signup')

        # 2. Creation Logic
        # We store the result in 'user' so we can log them in immediately
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            last_name=""
        )

        # 3. The "Direct Entry" Logic
        # This tells Django: "This person is authorized, don't ask for a password again yet."
        auth.login(request, user)

        # 4. Success Signal
        messages.success(request, f"Welcome, {username}! Redirecting to your dashboard...")

        return redirect('dashboard')

    return render(request, 'signup.html')
def login(request):
    if request.method == 'POST':
        # 1. THE GRAB
        u_name = request.POST.get('username')
        p_word = request.POST.get('password')

        # 2. THE VERIFIER (Literal Logic: "Does this pair exist?")
        user = auth.authenticate(username=u_name, password=p_word)

        if user is not None:
            # 3. THE HANDSHAKE: Success!
            auth.login(request, user)
            return redirect('dashboard')
        else:
            # 4. THE BOUNCER: Fail!
            messages.error(request, "Invalid username or password.")
            return redirect('login') # Stay on login page

    return render(request, 'login.html')