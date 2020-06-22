from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import TemplateView, View, FormView
from .forms import ConnectionForm, RegisterForm
from .models import User


class RegistrationView(FormView):
    form_class = RegisterForm

    def get(self, request):
        return render(request, "user/register.html", {"form": RegisterForm()})

    def post(self, request):
        """Method Description.
        Description details here (if needed).
        
        Args:
            name (type): Description. Default to False.
        
        Raises:
        Returns:
        """
        email = request.POST.get("email")
        password = request.POST.get("password1")
        extra_fields = {
            "first_name": request.POST.get("first_name"),
            "last_name": request.POST.get("last_name"),
        }
        User.objects.create_user(email=email, password=password, **extra_fields)
        return redirect("/")


def connection(request):
    """Method Description.
    Description details here (if needed).
    
    Args:
        name (type): Description. Default to False.
    
    Raises:
    Returns:
    """

    error = False

    if request.method == "POST":
        form = ConnectionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect("/")
            else:
                error = True
    else:
        form = ConnectionForm()

    return render(request, "user/connection.html", locals())


def disconnection(request):
    """Method Description.
    Description details here (if needed).
    
    Args:
        name (type): Description. Default to False.
    
    Raises:
    Returns:
    """

    logout(request)
    return redirect("/")
