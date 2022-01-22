
from email.mime import base
from xml.etree.ElementInclude import include
from django.contrib import admin
from index.views import fruitsViewSets, regionViewSets
from django.urls import path, include
from rest_framework import routers 


router = routers.DefaultRouter()


router.register(r'api', fruitsViewSets, regionViewSets)


urlpatterns = [
   
    path('admin/', admin.site.urls),
     path('', include(router.urls)),
   
 
   
    
] 
