from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


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
    return render(request, 'eventos.html',{"Usuario":request.user})

def agregar_eventos(request):
    return render(request, 'agregar_evento.html')


def confirmacion_registro(request):
    send_mail(
            subject = "¡Bienvenido al Torneo! Confirmación de Registro Exitoso",
            message = "Es un placer darte la más cordial bienvenida al Torneo organizado por TorneosGamingsRD. Nos complace enormemente confirmar que tu registro ha sido recibido y procesado exitosamente."
            ""
        "\n\n¡Felicidades! Has dado el primer paso hacia una experiencia de juego emocionante y llena de diversión. Nos complace enormemente contar contigo como parte de nuestra comunidad de jugadores apasionados."

        "\n\n¡Que empiece la competición y que la suerte esté siempre de tu lado!"

        "\n\nAtentamente,"

        "\n\nRuddy Contreras"
        "\nTorneosGamingsRD"
        "\nCreador de TorneosGamingsRD",
            recipient_list = [request.POST.get('email')],
            from_email = None,
            #from_email is only required to be filled if you do not want to use the value in our settings
            fail_silently=False,
        )
    return render(request, 'confirmacion_registro.html')

