#from django.shortcuts import render
from authuser.models import User
from django.shortcuts import render, redirect
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from authuser.forms import UserRegisterForm


def register_view(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        #last_name = request.POST.get('last_name')
        
        # Check if username is already taken
        if User.objects.filter(email=email).exists():
            messages.error(request, "Votre addresse mail est déjà prise!!")
            return render(request, 'auth/register.html', {'form':form})
        
        # Create the new user object
        user = User.objects.create_user(username=username, password=password, email=email, telephone=telephone)
        
        # Authenticate and log in the user
        user = authenticate(email=email, password=password)
        login(request, user)
        messages.success(request, f"Hey {username}, votre compte a été créé avec succès")
        return redirect('app:home') # Replace 'home' with your own URL name
    else:

        return render(request, 'auth/register.html', {'form':form})


def login_page(request):

    if request.user.is_authenticated:
        return redirect("app:home")
    
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                #messages.success(request, "Vous êtes connecté!!")
                return redirect("app:home")
            else:
                messages.error(request, "Cet utilisateur n'existe pas, veillez créer un compte!!")
                #return redirect(request, "authuser:register")
        except:
            messages.error(request, "erreur,veillez reessayer!!")
            #return redirect("authuser:login")

    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    return redirect("authuser:login")
