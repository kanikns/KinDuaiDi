from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    friend_list = [
        {'id': 1, 'name': 'Tiffany Young'},
        {'id': 2, 'name': 'Tiffany Young'},
        {'id': 3, 'name': 'Tiffany Young'}
    ]
    
    context = {
        'friend_name': 'Tiffany Young',
        'friend_list': friend_list
    }
    
    return render(request, template_name='findfriend/index.html', context=context)

def detail(request, friend_id):
    return HttpResponse("Detail of join party %s." % (str(friend_id)))