"""ycDataView URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
import dataView.views as dv

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^sayHello/', dv.sayHello),
    # url(r'^showStudents/', dv.showStudents),
    # url(r'^index/', include('dataView.urls')),
    url(r'^index_two/', dv.index_two),
    url(r'^index_check/', dv.index_check),
    url(r'^index_hotel/', dv.index_hotel),
    url(r'^index_hotel_check/', dv.index_hotel_check),
]
