from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.

# def index(request):
#     return HttpResponse('<h1>Hey, Welcome</h1>')


# def index(request):
#     #name = 'Shubham'
#     # context = {
#     #     'name':'Shubham',
#     #     'status':'Evening'
#     # }
#     return render(request,'index.html')#,context)  #  <==send dynamic data to our template file


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})



def index(request):
    # feature1 = Feature()
    # feature1.id = 1
    # feature1.name = 'Fast'
    # feature1.details = 'Our service is very quick'

    # feature2 = Feature()
    # feature2.id = 2
    # feature2.name = 'Weigh'
    # feature2.details = 'Our service is very Fast'

    features = Feature.objects.all()
    return render(request,'index.html', {'feature2':features})



def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if  password == password2:
           if User.objects.filter(email=email).exists():
              messages.info(request, 'Email Already Used')
              return redirect('register')
           elif User.objects.filter(username=username).exists():
               messages.info(request, 'Username Already Used')
               return redirect('register')
           else:
               user = User.objects.create_user(username=username, email=email, password=password)
               user.save();
               return redirect('login')
        else:
            messages.info(register, 'Password Not The Same')
            return redirect('register')   

    else:
        return render(request,'register.html')
    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
        
    else:    
        return render(request, 'login.html')    
    



def logout(request):
    auth.logout(request)
    return redirect('/')    


def post(request, pk):
    return render(request, 'post.html', {'pk':pk})