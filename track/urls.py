"""
URL configuration for benisuef project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from django.urls import path
from .views import *

urlpatterns = [
    path('',hello),
    path('Add/',newtrack,name='newtrack'),
    path('List/',alltracks,name='Tracks'),
    path('<int:id>/',trackbyid,name='TrackByID'),
    path('<str:name>/',trackbyname,name="TrackByName"),
    path('Update/<int:id>/',trackupdate,name="TrackUpdate"),
    path('Delete/<int:id>/',trackdelete,name="TrackDelete"),

]
