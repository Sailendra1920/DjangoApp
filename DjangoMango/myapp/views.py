from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Username
# Create your views here.
def register(request):
    users = Username.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        gender = request.POST['gender']

        add_user = Username(name=name, gender=gender)
        add_user.save()
        return redirect('register')

    return render(request, 'myapp/base.html', {'users': users})