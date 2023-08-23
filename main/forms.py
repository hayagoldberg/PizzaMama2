from django import forms
from .models import Order, Pizza


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'customer_phone', 'customer_address']

    pizzas = forms.ModelMultipleChoiceField(queryset=Pizza.objects.all(), widget=forms.CheckboxSelectMultiple)
    quantities = forms.TypedMultipleChoiceField(choices=[(str(i), i) for i in range(1, 11)], coerce=int, initial=1, widget=forms.CheckboxSelectMultiple)

    def save(self, commit=True):
        order = super().save(commit=False)
        order.save()

        pizzas = self.cleaned_data['pizzas']
        quantities = self.cleaned_data['quantities']

        for pizza, quantity in zip(pizzas, quantities):
            OrderedPizza.objects.create(order=order, pizza=pizza, quantity=quantity)

        return order
