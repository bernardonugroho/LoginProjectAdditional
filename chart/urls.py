from django.urls import path

from . import views

urlpatterns = [
    path('viewbar', views.viewbar, name = 'viewbar'),
    path('viewbubble', views.viewbubble, name = 'viewbubble'),
    path('viewpie', views.viewpie, name = 'viewpie'),
    path('viewdynamic', views.viewdynamic, name = 'viewdynamic'),
    path('viewmultiple', views.viewmultiple, name = 'viewmultiple'),
    path('viewmap', views.viewmap, name = 'viewmap'),
    path('viewgeo', views.viewgeo, name = 'viewgeo'),
 ]
