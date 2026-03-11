from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',index, name='index'),
    path('menu/',menu, name='menu'),
    path('about/',about, name='about'),
    path('contact/',contact, name='contact'),
    path('service/',service, name='service'),
    path('testemonial/',testemonial, name='testemonial'),
    # auth part
    path('register/',register, name='register'),
    path('log_in/',log_in, name='log_in'),
    path('logout/',log_out, name='log_out'),
    path('email_verify/',verify_email, name='email_verify'),
    path('password_change/',password_change,name='password_change'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html', html_email_template_name ='accounts/send_email.html'), name='password_reset'),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = "accounts/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = "accounts/password_reset_complete.html"), name='password_reset_complete'),
    
]

