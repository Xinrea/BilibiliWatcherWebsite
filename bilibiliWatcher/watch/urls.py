from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('user/<slug:username>',views.manage,name='manage'),
    path('<int:id>',views.dynamic,name='dynamic'),
    path('all/',views.dynamic_all,name='dynamic_all'),
    path('video/',views.dynamic_video,name='dynamic_video'),
    path('text/',views.dynamic_text,name='dynamic_text'),
    path('statistic/',views.statistic,name='statistic'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
]