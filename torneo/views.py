from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def depuesindex(request, username):
    return HttpResponse("<h1>Hola %s </h1>" % username)

def torneo(request):
    return render(request, "torneo.html")

from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm

class LoginFormView(FormView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = '/'  # Página a la que redirigir después del inicio de sesión exitoso

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form, 'error_message': "Invalid username or password."})

def super_smash_bros(request):
    return render(request, 'super_smash_bros.html')

def fifa(request):
    return render(request, 'fifa.html')

def call_of_duty(request):
    return render(request, 'call_of_duty.html')

def eventos(request):
    return render(request, 'eventos.html')