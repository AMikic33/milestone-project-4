from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from books.models import Product

# Create your views here.


def view_bag(request):
    """ the bag content page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Adding quantity to the bag """

    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} tp your shopping bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Remove item from the bag """

    bag = request.session.get('bag', {})

    try:
        bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
