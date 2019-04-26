from django.shortcuts import render
from django.http import HttpResponse
from .models import Servicings
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# def home(request):
#     return HttpResponse("<h1>My Site...</h1>")



def home(request):
    return render(request, 'mysite/home.html', {'home_active' : True})

def about(request):
    return render(request, 'mysite/about.html', {'title' : 'About', 'about_active' : True,})

class ServiceCreateView(LoginRequiredMixin, CreateView):
    model = Servicings
    fields = ['service_type', 'service_description', 'service_location']

    def form_valid(self, form):
        form.instance.service_user = self.request.user
        return super().form_valid(form)
