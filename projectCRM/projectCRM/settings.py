# ---- ==== IMPORT Necessary Modules ==== ----
from pathlib import Path
import os
from django.urls import reverse_lazy


# ---- ==== Build paths inside the project like this: BASE_DIR / 'subdir'. ==== ----
BASE_DIR = Path(__file__).resolve().parent.parent


# ---- ==== Setting Up 'SECRET_KEY' and 'DEBUG' ==== ----
SECRET_KEY = os.environ.get("SECRET_KEY") 
DEBUG = (os.environ.get("DEBUG_VALUE") == "True")


# ---- ==== Defining the URL the project can Access By ===== ----
ALLOWED_HOSTS = [
    "CtrlCRM.pythonanywhere.com",
    "http://localhost:8000/",
    "http://127.0.0.1:8000/",
    "localhost",
    "127.0.0.1",
    "*"
]


# ---- ==== Related to Google Login SetUp ==== ----
SITE_ID = 3


# ---- ==== INSTALLED_APPS ==== ----
INSTALLED_APPS = [
    'featuredApp.apps.FeaturedappConfig',
    'client.apps.ClientConfig',
    'accounts.apps.AccountsConfig',
    'androidApplication.apps.AndroidapplicationConfig',

    'crispy_forms',
    'crispy_bootstrap4',
    'widget_tweaks',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # Android Application
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    'dj_rest_auth',
    'dj_rest_auth.registration',
    'rest_framework.authtoken',


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# ---- ==== SOCIAL ACCOUNTS used to Authenticate User ==== ----
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# ---- ==== ADDITIONAL SECURITY ==== ----
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

# ---- ==== Corsheaders for Android Application Developement ==== ----
MIDDLEWARE.insert(0, 'corsheaders.middleware.CorsMiddleware')
CORS_ALLOW_ALL_ORIGINS = True


# ---- ==== Root urls.py file Location ==== ----
ROOT_URLCONF = 'projectCRM.urls'


# ---- ==== Default template file Location ==== ----
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                # Custom processor
                'featuredApp.context_processor.accessible_accounts',
                'featuredApp.context_processor.feedback_form_processor',
            ],
        },
    },
]

# ---- ==== Additional Security ==== ----

WSGI_APPLICATION = 'projectCRM.wsgi.application'


# ---- ==== Database [Migration Needed!] ==== ----

# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ---- ==== Password validation ==== ----
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ---- ==== Internationalization ==== ----
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# ---- ==== Static files (CSS, JavaScript, Images) ==== ----
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = 'static/'


# ---- ==== Default primary key field type ==== ----
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ---- ==== DISCARD ITEM ==== ----
# No longer needed
# # Changed Auth model to BusinessUser which allows more specific fields..
# # company email; company name; + AbstractBaseUser + exceptional fields
# AUTH_USER_MODEL = 'accounts.BusinessUser'


# ---- ==== Authentication Backend ==== ----
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Default Django backend
    # 'allauth.account.auth_backends.AuthenticationBackend', # Cutom [GOOGLE LOGIN]
]


# ---- ==== Microsoft Login [Web Application] ==== ----
MSAL_CLIENT_ID = os.environ.get('MICROSOFT_CLIENT_ID')
MSAL_CLIENT_SECRET = os.environ.get('MICROSOFT_CLIENT_SECRET')
MSAL_AUTHORITY = "https://login.microsoftonline.com/common"  # or your tenant
MSAL_REDIRECT = "http://localhost:8000/get_token"
MSAL_SCOPES = ["User.Read"]


# ---- ==== Specific to Froms ==== ----
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# ---- ==== Media File Location ==== ----
# Added media path (to store logo of company and storing Documents)
# Secured folder can't be accessed directly
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ---- ==== Login and Logout Redirect ==== ----
LOGIN_REDIRECT_URL = reverse_lazy('profile')
LOGOUT_REDIRECT_URL = "/"


# ---- ==== Email SetUp ==== ----
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


# ---- ==== Specific to Mobile Application ==== ----
# JWT_AUTH_COOKIE = 'access'
# JWT_AUTH_REFRESH_COOKIE = 'refresh'
# TOKEN_MODEL = None
# SIMPLE_JWT = {
#     'AUTH_HEADER_TYPES': ('Bearer',),
# }
# REST_USE_JWT = True

REST_USE_JWT = True
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}


# ---- ==== DISCARD ITEMS ==== ----
# Set login page
# LOGIN_URL = 'login'


# ---- ==== Local development ==== ----
# if DEBUG:
#     import mimetypes
#     mimetypes.add_type("image/png", ".png", True)