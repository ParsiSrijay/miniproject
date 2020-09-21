from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',views.signup),
    path('signin',views.signin),
    path('crop_update',views.CropDetails, name = 'image_upload'),
    path('success', views.success, name = 'success'),
    path('display',views.displayOrder),
    path('confirm',views.confirm),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)