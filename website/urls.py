from django.urls import path

from website import views

app_name= 'website'
urlpatterns = [
    path('about', views.about, name = "about"),
    path('contact', views.contact, name = "contact"),
    path('index', views.index, name = "index"),
    path('gallery_single', views.gallery_single, name = "gallery-single"),
    path('gallery', views.gallery, name = "gallery"),
    path('sample_inner_page', views.sample_inner_page, name = "resume"),
    path('services', views.services, name = "services"),

    ### for user registratio, sign-in sign-out
    path('base', views.base, name = 'base'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login_reg'),
    path('logout', views.logoutuser, name = 'logout'),
]