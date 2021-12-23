from django.urls import path,include
from django.conf.urls import url
from .views import upload,stream

app_name= 'ui'

urlpatterns = [

    url(r'^upload$', upload),
    url(r'^stream$', stream)

]
