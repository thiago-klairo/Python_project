from pdb import post_mortem
from django.views.generic import DetailView, ListView
from .models import Fruits, Region
from django.shortcuts import render
from rest_framework import viewsets
from index.serializer import regionSerializer, fruitsSerializer



class regionViewSets(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class =  regionSerializer  


class fruitsViewSets(viewsets.ModelViewSet):
    queryset = Fruits.objects.all() 
    serializer_class = fruitsSerializer 






class ListRegion(ListView):
    model = Region

class RegionDetailView(DetailView):
        model = Region


 



        
def regionFunc(request, pk ):
            region = Region.objects.filter(id = pk)
            return render(request, 'templates/region_list.html' , {'Região': region, 'pk:' : pk})
            