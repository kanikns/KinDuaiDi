from django.contrib.auth.models import User
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse, Http404
# Create your views here.
from item.models import Item

from borrow.models import Borrow, Borrow_Item


def item(request):
    username = None
    if not request.user.is_authenticated:
        return redirect('/')

        # return redirect('account/login')
    # user = User.objects.get(username=request.user.username)
    item_list = Item.objects.all()
    context = {
        'item_list': item_list,
    }
    return render(request, 'item/main-item.html', context)