"""instageek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token

from instageek.views import FollowersAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/obtain-token/', obtain_auth_token),  # devuelve token haciendo un POST con username y password
    url(r'^api/rest-auth/', include('rest_auth.urls')),
    url(r'^api/rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^api/token-refresh/', refresh_jwt_token),
    url(r'^api/token-verify/', verify_jwt_token),
    url(r'^oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^accounts/', include('allauth.urls')),

    #conexion con microservicio de followers
    url(r'^api/follow-friend/', FollowersAPIView.as_view())

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
