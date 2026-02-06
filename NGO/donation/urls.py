from django.urls import path
from . import views

urlpatterns = [
    #admin
    path('', views.index),
    path('admin_login/', views.admin_login),
    path('admin_dashboard/', views.admin_dashboard),
    path('add_ngo/', views.add_ngo),
    path('view_ngos/', views.view_ngos),
    path('view_donations/', views.view_donations),

#user
    path('register/', views.register),
    path('user_login/', views.user_login),
    path('user_dashboard/', views.user_dashboard),
    path('user_ngos/', views.user_ngos),
    path('donate/<int:ngo_id>/', views.donate),


    path('add_volunteer/', views.add_volunteer),
    path('view_volunteer_opportunities/', views.view_volunteer_opportunities),
    path('view_volunteers/', views.view_volunteers),


    path('user_volunteer_opportunities/', views.user_volunteer_opportunities),
    path('enroll_volunteer/<int:opp_id>/', views.enroll_volunteer),


    path('logout/', views.logout),
]
