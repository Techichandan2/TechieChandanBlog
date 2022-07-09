from django.urls import path
from django.contrib.auth import views as auth_views
from users import views
from .form import MyPasswordResetForm,MySetPasswordForm




urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.Login, name='login'),
    path('logout/', views.Logout, name='logout'),
    path('change_password/', views.ChangePass, name='changepass'),
    path('contact/', views.contact, name='contact'),
    #reset password
    
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="users/password_reset_form.html", form_class=MyPasswordResetForm), name='password_reset_form'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html',form_class=MySetPasswordForm), name='password_reset_confirm'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'), name='password_reset_complete')
]