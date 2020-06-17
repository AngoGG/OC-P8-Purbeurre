from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render
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
            user = authenticate(
                username=username, password=password
            )  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else:  # sinon une erreur sera affichée
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
