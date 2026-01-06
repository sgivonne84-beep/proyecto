from django.shortcuts import render,redirect
from .models import Aviso, Noticia, Colaborador
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

#agregado
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from .forms import AvisoForm, NoticiaForm, ColaboradorForm

from django.contrib.auth.forms import AuthenticationForm
from .models import MensajeContacto




def inicio(request):
    #mueatra un poco de todo
    ctx = {
        'avisos': Aviso.objects.order_by('-fecha_publicacion')[:4],
         'noticias': Noticia.objects.order_by('-fecha_publicacion')[:4],
          'colaboradores': Colaborador.objects.all()[:8],
    }
    return render(request, 'inicio.html', ctx)

def avisos(request):
    return render(request, 'avisos.html', {'avisos': Aviso.objects.order_by('-fecha_publicacion')})

def noticias(request):
    return render(request, 'noticias.html', {'noticias': Noticia.objects.order_by('-fecha_publicacion')})

def colaboradores(request):
    return render(request, 'colaboradores.html', {'colaboradores': Colaborador.objects.all()})

def contacto(request):
    return render(request, 'contacto.html')


def login(request):
    return render(request, 'registration/login.html')



#agregado12334
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('aviso_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')


#agregado
@login_required
def aviso_list(request):
    avisos = Aviso.objects.all()
    return render(request, 'aviso_list.html', {'avisos': avisos})

@login_required
def aviso_create(request):
    if request.method == 'POST':
        form = AvisoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('aviso_list')
    else:
        form = AvisoForm()
    return render(request, 'aviso_form.html', {'form': form})

@login_required
def aviso_update(request, pk):
    aviso = Aviso.objects.get(pk=pk)
    if request.method == 'POST':
        form = AvisoForm(request.POST, instance=aviso)
        if form.is_valid():
            form.save()
            return redirect('aviso_list')
    else:
        form = AvisoForm(instance=aviso)
    return render(request, 'aviso_form.html', {'form': form})

@login_required
def aviso_delete(request, pk):
    aviso = Aviso.objects.get(pk=pk)
    if request.method == 'POST':
        aviso.delete()
        return redirect('aviso_list')
    return render(request, 'aviso_confirm_delete.html', {'aviso': aviso})

#NOTICIA

@login_required
def noticia_list(request):
    noticias = Noticia.objects.all().order_by('-fecha_publicacion')
    print(noticias)
    return render(request, 'noticia_list.html', {'noticias': noticias})

@login_required
def noticia_create(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('noticia_list')
        else:
            print(form.errors)
            return render(request, 'noticia_form.html', {'form': form, 'error': 'Error al crear'})
    else:
        form = NoticiaForm()
    return render(request, 'noticia_form.html', {'form': form})

@login_required
def noticia_update(request, pk):
    noticia = Noticia.objects.get(pk=pk)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            return redirect('noticia_list')
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'noticia_form.html', {'form': form})

@login_required
def noticia_delete(request, pk):
    noticia = Noticia.objects.get(pk=pk)
    if request.method == 'POST':
        noticia.delete()
        return redirect('noticia_list')
    return render(request, 'noticia_confirm_delete.html', {'noticia': noticia})

#COLABORADOR
@login_required
def colaborador_list(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'registration/colaborador_list.html', {'colaboradores': colaboradores})

@login_required
def colaborador_create(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('colaborador_list')
    else:
        form = ColaboradorForm()
    return render(request, 'registration/colaborador_form.html', {'form': form})

@login_required
def colaborador_update(request, pk):
    colaborador = Colaborador.objects.get(pk=pk)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, request.FILES, instance=colaborador)
        if form.is_valid():
            form.save()
            return redirect('colaborador_list')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'registration/colaborador_form.html', {'form': form})

@login_required
def colaborador_delete(request, pk):
    colaborador = Colaborador.objects.get(pk=pk)
    if request.method == 'POST':
        colaborador.delete()
        return redirect('colaborador_list')
    return render(request, 'registration/colaborador_confirm_delete.html', {'colaborador': colaborador})

#agregado12
def inicio2(request):
    avisos = Aviso.objects.all()
    noticias = Noticia.objects.all()
    colaboradores = Colaborador.objects.all()
    return render(request, 'inicio2.html', {'avisos': avisos, 'noticias': noticias, 'colaboradores': colaboradores})

#contarcto agregado

def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        # Aquí puedes guardar en la BD o enviar correos
        print("Nombre:", nombre)
        print("Email:", email)
        print("Mensaje:", mensaje)

        messages.success(request, "Tu mensaje ha sido enviado con éxito.")
        return redirect("contacto")

    return render(request, "contacto.html")

def contacto(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        email = request.POST.get("email")
        mensaje = request.POST.get("mensaje")

        MensajeContacto.objects.create(
            nombre=nombre,
            email=email,
            mensaje=mensaje
        )

        messages.success(request, "Tu mensaje ha sido enviado con éxito.")
        return redirect("contacto")

    return render(request, "contacto.html")


@login_required
def contacto2(request):
    mensajes = MensajeContacto.objects.order_by('-id')
    return render(request, 'contacto2.html', {'mensajes': mensajes})
