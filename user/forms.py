#!/usr/bin/env python3
"""
@desc    description
@author  ANGO <ango@afnor.org>
@version 0.0.1
@date    2020-06-02
@note    0.0.1 (2020-06-02) : Init file
"""
from django import forms


class ConnectionForm(forms.Form):
    """Class description.
    Description details here (if needed).
    
    Attributes:
        name (type): Description. Default to False.
    """

    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)
