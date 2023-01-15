from django.shortcuts import render, redirect, get_object_or_404
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sorting = {'name': 'name',
               'max_price': '-price',
               'min_price': 'price'        
    }
    template = 'catalog.html'
    
    phone = Phone.objects.all().order_by(sorting[request.GET.get('sort', 'name')])
    
    context = {'phones': phone}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = get_object_or_404(Phone, slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
