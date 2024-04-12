from django.shortcuts import render
from user.models import User



def info_client(request):
    user = User.objects.all()
    context = {
        'user': user
    }

    return render(request, 'user/info_client.html', context=context)