from django.shortcuts import render, redirect, get_object_or_404
from ..models import Address
from ..forms import AddressForm


def create_address(request):
    form = AddressForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_address')

    return render(request, 'ubs/address/create.html', {'form': form})


def list_address(request):
    addresses = Address.objects.all()
    return render(request, 'ubs/address/list.html', {'addresses': addresses})


def update_address(request, id):
    address = get_object_or_404(Address, id=id)
    form = AddressForm(request.POST or None, instance=address)

    if form.is_valid():
        form.save()
        return redirect('list_address')

    return render(request, 'ubs/address/update.html', {'form': form})


def delete_address(request, id):
    address = get_object_or_404(Address, id=id)

    if request.method == "POST":
        address.delete()
        return redirect('list_address')

    return render(request, 'ubs/address/delete.html', {'address': address})