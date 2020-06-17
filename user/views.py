from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse
from .forms import ConnectionForm


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
                return redirect("/products/")
            else:
                error = True
    else:
        form = ConnectionForm()

    return render(request, "user/connection.html", locals())


def disconnection(request):
    """Class description.
    Description details here (if needed).
    
    Attributes:
        name (type): Description. Default to False.
    """

    logout(request)
    return redirect(reverse(connection))
