"""meeting_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
<<<<<<< HEAD

=======
>>>>>>> 1656026343d2bdeaf4bb6a3d86c32cb9a9a01c98

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('website.urls', namespace='website')),
<<<<<<< HEAD
    path('account/api/', include('account.api.urls', namespace='account_api')),
    path('website/api/', include('website.api.urls', namespace='website_api')),
=======
>>>>>>> 1656026343d2bdeaf4bb6a3d86c32cb9a9a01c98
    path('account/', include('account.urls', namespace='account')),
]
## JUST DEVELOPMENT PURPOSE, NOT USE IN PRODUCTION

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)