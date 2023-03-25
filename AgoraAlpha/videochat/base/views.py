from django.shortcuts import render
from django.http import JsonResponse
from agora_token_builder import RtcTokenBuilder
import random
import time
# Create your views here.

def getToken(request):

    appId = 'd025a07a47a4421db20529206dba7b3b'
    appCertificate = 'f90fd1d3603d4d32a4ba711eace799bd'
    channelName = request.GET.get('channel')
    uid = random.randint(1,230)
    expirationTimeInSec = 3600*24
    currentTimeStamp = time.time()
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSec
    role = 1 

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)
    return JsonResponse({'token':token, 'uid':uid}, safe=False)

def lobby(request):
    return render(request,'base/lobby.html')

def room(request):
    return render(request, 'base/room.html')