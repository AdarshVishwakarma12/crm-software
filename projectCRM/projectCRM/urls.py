from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# Views from accounts
from accounts.views import indexView
from accounts.views import aboutView
from accounts.views import registrationView
from accounts import views as accountViews

# Views from featuredApp
from featuredApp.views import profile_view

# for Authentication - Login and Logout
from django.contrib.auth import views as auth_views

# URL's!
urlpatterns = [

    # Index / Home Page [WELCOME PAGE]
    path('', indexView, name='index'),
    path('home/', indexView, name='home'),
    path('about/', aboutView, name='about'),

    # Google Sign-up / Log-in
    path("accounts/", include("allauth.urls")),

    # Microsoft Sign-up / Log-in
    path('signin', accountViews.sign_in, name='signin'),
    path('get_token', accountViews.get_token, name='get_token'),
    path('signout', accountViews.sign_out, name='signout'),

    # Creating New User [Registration Page]
    path('register/', registrationView, name='register'),

    # Login and Logout
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Profile View
    path('accounts/profile/', profile_view, name='profile'),

    # Admin Page for Local Development
    path('admin/', admin.site.urls),

    # !!! Advanced Featured App !!!
    path('apps/', include('featuredApp.urls')),

]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)