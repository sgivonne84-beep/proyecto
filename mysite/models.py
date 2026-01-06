from django.db import models

# Create your models here.
class Aviso(models.Model):
    id_aviso = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, verbose_name="Titulo del aviso")
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicacion")
    
    def __str__(self):
        return self.titulo

class Noticia(models.Model):
    id_noticia = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fotografia = models.ImageField(upload_to='noticias/', blank=True, null=True)

    def __str__(self):
            return self.titulo
    
class Colaborador(models.Model):
    id_colaborador= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    fotografia = models.ImageField(upload_to='colaboradores/', blank=True, null=True)

    def __str__(self):
        return self.nombre
    
class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"
