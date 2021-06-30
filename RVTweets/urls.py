"""RVTweets URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path, include  # url()
from django.views.generic import TemplateView
from covnews.views import news
from donations.views import add_donation, donations_main

from accounts.views import (
    login_view,
    logout_view,
    register_view,
)

from tweets.views import (
    home_view,
    tweets_list_view,
    tweets_detail_view,

)

urlpatterns = [
    path('', tweets_list_view),
    path('admin/', admin.site.urls),
    path('global/', tweets_list_view),
    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
    path('<int:tweet_id>', tweets_detail_view),
    path('news/', news),
    path('donations/', donations_main),
    path('donations/details', add_donation, name='donation-form'),
    path('news/map/', TemplateView.as_view(template_name="map.html"),
         name='map'),
    re_path(r'profiles?/', include('profiles.urls')),
    path('api/tweets/', include('tweets.api.urls')),
    re_path(r'api/profiles?/', include('profiles.api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
