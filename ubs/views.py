from django.shortcuts import render, redirect, get_object_or_404 
from .forms import AddressForm
from .models import Address

def home(request):
    lista = Address.objects.all()
    return render(request, "ubs/home.html", {'endereços': lista})

def login(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/ubs/")
    else:
        form = AddressForm()

    return render(request,"ubs/login.html", {"form": form} )

def endereco(request,id):
    endereco = get_object_or_404(Address, id=id)
    return render(request, "ubs/endereco.html", {'endereco': endereco})
