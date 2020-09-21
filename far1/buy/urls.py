from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',views.signup),
    path('signin',views.signin),
    path('placeorder',views.placeorder),
    path('confirm',views.confirm),
    path('orders',views.orderlist),
]
