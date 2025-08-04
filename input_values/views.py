
from .models import MyModel
from django.shortcuts import redirect, render

def index(request):
    return render(request, 'forms/main.html')

def sobre(request):
    return render(request, 'forms/sobre.html')

def submit_form(request):
    if request.method == "POST":
        new_instance = MyModel(
            name = request.POST.get('name'),
            email = request.POST.get('email'),
            phone = request.POST.get('phone'),
            instagram = request.POST.get('instagram'),
            by = request.POST.get('by'),
            motivo = request.POST.get('motivo')
        )

        # 2. Salve a instância no banco de dados (realiza o INSERT)
        new_instance.save()
    return render(request, 'forms/success.html')