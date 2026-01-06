from django.urls import path
from . import views
from .views import aviso_list, aviso_create, aviso_update, aviso_delete
from .views import login_view, logout_view
from .views import noticia_list, noticia_create, noticia_update, noticia_delete
from .views import colaborador_list, colaborador_create, colaborador_update, colaborador_delete
from .views import inicio2
from .views import contacto2

urlpatterns=[
    path('', views.inicio, name='inicio'),
    path('avisos/', views.avisos, name='avisos'),
    path('noticias/', views.noticias, name='noticias'),
    path('colaboradores/', views.colaboradores, name='colaboradores'),
    path('contacto/' , views.contacto, name='contacto'),

    path('contacto2/', views.contacto2, name='contacto2'),

    path('login/', views.login_view, name='login'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    #agregado
    path('aviso/', aviso_list, name='aviso_list'),
    path('aviso/create/', aviso_create, name='aviso_create'),
    path('aviso/<pk>/update/', aviso_update, name='aviso_update'),
    path('aviso/<pk>/delete/', aviso_delete, name='aviso_delete'),

    path('noticia/', noticia_list, name='noticia_list'),
    path('noticia/create/', noticia_create, name='noticia_create'),
    path('noticia/<pk>/update/', noticia_update, name='noticia_update'),
    path('noticia/<pk>/delete/', noticia_delete, name='noticia_delete'),

    path('colaborador/', colaborador_list, name='colaborador_list'),
    path('colaborador/create/', colaborador_create, name='colaborador_create'),
    path('colaborador/<pk>/update/', colaborador_update, name='colaborador_update'),
    path('colaborador/<pk>/delete/', colaborador_delete, name='colaborador_delete'),
   

    path('inicio2', inicio2, name='inicio2'),
    

]


 
