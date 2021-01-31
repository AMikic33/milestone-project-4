from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "The shopping bag is empty")
        return redirect(reverse('books'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IFhobCKSTpFAnpJLQLXCCX8bFjZJd3Jztb6cTmXAkCXnEZtDO7aFMaD9Ey3YtHPDcJjZyy1gs1RCPZJchLkvZFC00fNYGaOV2',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
