from django.shortcuts import render, HttpResponse
from .models import Pizza, Order
from .forms import OrderForm


# Create your views here.


def index_view(request):
    return render(request, 'main/index.html')


def menu_view(request):
    pizzas = Pizza.objects.all().order_by('price')
    context = {'pizzas': pizzas}
    return render(request, 'main/menu.html', context)


def order_view(request):
    pizzas = Pizza.objects.all()

    if request.method == 'POST':
        form = OrderForm(request.POST)

        if form.is_valid():
            form.save()
            # order.calculate_total()  # Assuming you have a method to calculate the total price
            return HttpResponse('votre commande a ete enregistre')
        else:
            return HttpResponse('form not valid')
    else:
        form = OrderForm()

    return render(request, 'main/order_form.html', {'pizzas': pizzas, 'form': form})
