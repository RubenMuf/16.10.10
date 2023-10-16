"""
URL configuration for djangoProject_saita project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('kino/', views.Kino_list.as_view(), name='allkino'),
    path('kino/<slug:pk>/<str:title>', views.Kino_detail.as_view(), name='info_movie'),

    path('actor/', views.Actor_list.as_view(), name='allactor'),
    path('actor/<slug:pk>/<str:lname>', views.Actor_detail.as_view(), name='info_actor'),

    path('director/', views.Director_list.as_view(), name='alldirector'),
    path('director/<slug:pk>/<str:lname>', views.Director_detail.as_view(), name='info_director'),
    # path('kino/<int:id>/', views.info, name='info'),
    path('user/', include('django.contrib.auth.urls')), # чтобы юзеры могли заходить на сайт в кабинет за счет переадресации include
    path('status/', views.status, name='status'),
    path('status/prosmotr/<int:id1>/<int:id2>/<int:id3>', views.prosmotr, name='prosmotr'),
    path('status/buy/<int:type>/', views.buy, name='buystatus'),
    path('user/registr/', views.registr, name='registr'),

    path('status/purchase/', views.purchase, name='purchase'),
    path('status/del/<int:t1>/', views.del_, name='del_'),
    path('status/app/<int:type_>/', views.app_, name='app_')


]
'''
login
reset_form
reset_done
reset_confirm
reset_complete
'''