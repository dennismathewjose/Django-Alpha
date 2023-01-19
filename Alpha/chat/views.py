from django.shortcuts import render
# Create your views here.
def videocallview(request):
    return render(request, 'chat/vdoui.html')
