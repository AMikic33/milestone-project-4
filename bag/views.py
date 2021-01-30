from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ the bag content page """

    return render(request, 'bag/bag.html')