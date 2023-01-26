from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def videocallview(request):
    return render(request, 'chat/vdoui.html')
