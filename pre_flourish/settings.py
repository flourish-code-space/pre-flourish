"""
Django settings for pre_flourish project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1mge7y#g2-f^qv0vvhdkw*2km%_3r%lt6*$e3ks6ujq9ts)u&y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

APP_NAME = 'pre_flourish'

LOGIN_REDIRECT_URL = 'home_url'

ETC_DIR = '/etc'

SITE_ID = 40

ALLOWED_HOSTS = []

INDEX_PAGE = 'pre_flourish.bhp.org.bw'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crypto_fields.apps.AppConfig',
    'django.contrib.sites',
    'edc_action_item.apps.AppConfig',
    'edc_consent.apps.AppConfig',
    'edc_dashboard.apps.AppConfig',
    'edc_device.apps.AppConfig',
    'edc_identifier.apps.AppConfig',
    'edc_lab.apps.AppConfig',
    'edc_locator.apps.AppConfig',
    'edc_model_admin.apps.AppConfig',
    'edc_navbar.apps.AppConfig',
    'edc_prn.apps.AppConfig',
    'edc_registration.apps.AppConfig',
    'edc_subject_dashboard.apps.AppConfig',
    'edc_visit_schedule.apps.AppConfig',
    'pre_flourish.apps.EdcAppointmentAppConfig',
    'pre_flourish.apps.EdcBaseAppConfig',
    'pre_flourish.apps.EdcFacilityAppConfig',
    'pre_flourish.apps.EdcProtocolAppConfig',
    'pre_flourish.apps.EdcTimepointAppConfig',
    'pre_flourish.apps.EdcVisitTrackingAppConfig',
    'pre_flourish.apps.AppConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'edc_dashboard.middleware.DashboardMiddleware',
    'edc_subject_dashboard.middleware.DashboardMiddleware',
]

ROOT_URLCONF = 'pre_flourish.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'pre_flourish.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DEFAULT_APPOINTMENT_MODEL = 'edc_appointment.appointment'

COUNTRY = 'botswana'
HOLIDAY_FILE = os.path.join(BASE_DIR, 'holidays.csv')

DASHBOARD_URL_NAMES = {
    'pre_flourish_screening_listboard_url': 'pre_flourish_screening_listboard_url',
    'pre_flourish_consent_listboard_url': 'pre_flourish_consent_listboard_url',
    'pre_flourish_child_listboard_url': 'pre_flourish_child_listboard_url',
    'pre_flourish_subject_dashboard_url': 'pre_flourish_subject_dashboard_url',
}

DASHBOARD_BASE_TEMPLATES = {
    'listboard_base_template': 'pre_flourish/base.html',
    'dashboard_base_template': 'pre_flourish/base.html',
    'pre_flourish_child_listboard_template': 'pre_flourish/child/child_listboard.html',
    'pre_flourish_subject_dashboard_template': 'pre_flourish/caregiver/dashboard.html',
    'pre_flourish_screening_listboard_template': 'pre_flourish/caregiver/listboard.html',
    'pre_flourish_subject_listboard_template': 'pre_flourish/caregiver/subject_listboard.html',
    }

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

PARENT_REFERENCE_MODEL1 = ''
PARENT_REFERENCE_MODEL2 = ''
