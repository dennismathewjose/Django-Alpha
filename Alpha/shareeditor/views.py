from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from chat.models import Chat
# Create your views here.
def editor(request):
    if request.method == 'POST':
        u_name = request.POST['chat-username']
        get_room = Chat.objects.filter(room_name = u_name)
        if get_room:
            c = get_room[0]
            number = c.allowed_users
            if int(number) < 2:
                number = 2
                return redirect(f'/chat/{u_name}/join/')
        else:
            create = Chat.objects.create(room_name=u_name,allowed_users=1)
            if create:
                return redirect(f'/chat/{u_name}/created/')
    return render(request, 'chat/vdoui.html')


