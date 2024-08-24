from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('signup/', views.registerPage, name="signup"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('settings/', views.settingsPage, name="settings"),
    path('add_photo/', views.addPhoto, name="add_photo"),
    path('view_photo/<int:photo_id>/', views.viewPhoto, name="view_photo"),
    path('delete_photo/<int:photo_id>/', views.deletePhoto, name='delete_photo'),
    path('delete_account/', views.deleteAccount, name="delete_account"),
    path('change_password/', auth_views.PasswordChangeView.as_view(template_name="myapp/change_password.html"), name="password_change"),
    path('change_password_complete/', auth_views.PasswordChangeDoneView.as_view(template_name="myapp/change_password_complete.html"), name="password_change_done"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="myapp/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="myapp/password_reset_sent.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="myapp/password_reset_form.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="myapp/password_reset_complete.html"), name="password_reset_complete"),
]