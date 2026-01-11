from django.contrib.auth.models import User

def create_admin():
    # Solo crea el superusuario si no existe
    if not User.objects.filter(username='Usuario13').exists():
        User.objects.create_superuser(
            username='Usuario13',
            email='ivonne@gmail.com',
            password='ivonne13'
        )
        print("Superusuario creado ✅")
    else:
        print("Superusuario ya existe")