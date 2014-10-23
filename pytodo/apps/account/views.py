from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

def index(request):
    args = {
            'user': 'Gonzalo'
            }
    return render_to_response('account/index.html', args)

def new(request):
    args = {
            'user': 'Gonzalo'
            }
    return render_to_response('account/new.html', args)

def profile(request):
    args = {
            'user': 'Gonzalo'
            }
    return render_to_response('account/profile.html', args)

def holas(request):
    args = {
            'user':'Gonzalo'
            }
    return render_to_response('account/profile.html', args)
