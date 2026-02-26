from django.contrib import admin
from django.urls import path
from Admin import views

urlpatterns = [
    # 1. Django's built-in admin (Leave this as is)
    path('admin/', admin.site.urls),

    # 2. Your custom App paths
    path('', views.dashboard, name='dashboard'),
    path('additem/', views.add_item, name='add_item'),

    # 3. Dynamic path: This fixes the "missing id" error.
    # The <int:id> tells Django to expect a number here (e.g., /updateitem/5/)
    path('updateitem/<int:id>/', views.update_item, name='Update_item'),
]