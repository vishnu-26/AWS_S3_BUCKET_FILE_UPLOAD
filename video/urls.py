from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include
from django.conf.urls import url
from .views import upload_file

app_name= 'video'

urlpatterns = [

    url(r'^upload$', upload_file),
    

] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
