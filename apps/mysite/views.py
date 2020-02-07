from django.shortcuts import render
from django.views.generic import ListView

class IndexListView(ListView):
    template_name = "main_page/index.html"

    def get_queryset(self, *args, **kwargs):
        return "not objects"

    
