# ---- ==== IMPORT STATEMENT GOES HERE ==== ----

# Basic
from django.shortcuts import render, redirect

# Registeration From (for creating new user)
from .forms import CompanyUserCreationForm

# User MODEL - Authentication and Authorization
from django.contrib.auth.models import User

# A helper notification section, which notify the new activity
from django.contrib import messages

# The Decorator, which allow the views to be accessed by only the login members
from django.contrib.auth.decorators import login_required


# ---- ==== VIEWS FILES GOES HERE ==== ----

# Index or Home page for CRM Software
def indexView(request, *args, **kwargs):

    if request.user.is_authenticated:
        user = request.user.businessuser
    else:
        user = None

    context = {
        'businessuser': user,
    }

    # print(request.path)

    return render(
        request, 
        'accounts/index.html',
        context,
    )

# About Page of CRM Software Include info about the Authors
def aboutView(request, *args, **kwargs):
    return render(request, 'accounts/about.html')

# Register a New Account
def registrationView(request, *args, **kwargs):
    if(request.method == "POST"):
        form = CompanyUserCreationForm(request.POST)
        if(form.is_valid()):
            form.save()
            companyName = form.cleaned_data.get("company_email")
            messages.success(request, f"Your account has been created! You can now log in")
            return redirect('login')
        else:
            messages.success(request, f"Can't Create Account")
    else:
        form = CompanyUserCreationForm()
    
    context = {
        'form': form,
    }

    return render(request, 'accounts/register.html', context)

# Login and Logout are handled from URL-Patterns Using default django Class.

# Profile View Extends featuredApp/base.html
@login_required
def profileView(request, *args, **kwargs):

    print(" I am here ")

    user = request.user.businessuser

    print(user.company_email)

    context = {
        'businessuser': user,
    }

    return render(
        request, 
        'accounts/profile.html',
        context,
    )

# ---- ==== Microsoft Login ==== ----
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth.models import User
import msal

# Start login
def sign_in(request):
    print('trying to sign in')

    # Create MSAL confidential client
    msal_app = msal.ConfidentialClientApplication(
        client_id=settings.MSAL_CLIENT_ID,
        client_credential=settings.MSAL_CLIENT_SECRET,
        authority=settings.MSAL_AUTHORITY,
    )

    print('initializing flow')

    flow = msal_app.initiate_auth_code_flow(
        scopes=settings.MSAL_SCOPES,
        redirect_uri=settings.MSAL_REDIRECT,
    )

    print('path: ', flow)
    request.session["auth_flow"] = flow
    return redirect(flow["auth_uri"])

# Callback to get token
def get_token(request):
    print('getting token')
    try:
        flow = request.session.pop("auth_flow")
        msal_app = msal.ConfidentialClientApplication(
            client_id=settings.MSAL_CLIENT_ID,
            client_credential=settings.MSAL_CLIENT_SECRET,
            authority=settings.MSAL_AUTHORITY,
        )
        result = msal_app.acquire_token_by_auth_code_flow(flow, request.GET)

        if "access_token" in result:
            request.session["user"] = result.get("id_token_claims")

            claims = result.get("id_token_claims")
            email = claims.get("preferred_username") or claims.get("email")
            name = claims.get("name") or email

            user, created = User.objects.get_or_create(username=email, defaults={"first_name": name})

            if not created and user.first_name != name:
                user.first_name = name
                user.save()
            
            login(request, user)

            return redirect("/")  # or home page
        else:
            return render(request, "error.html", {"error": result.get("error_description")})
    except Exception as e:
        return render(request, "error.html", {"error": str(e)})

# Logout
def sign_out(request):
    request.session.flush()
    return redirect("/")