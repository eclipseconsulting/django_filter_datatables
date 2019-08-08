from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login', views.LogInView.as_view(), name='login'),
    path('logout', views.LogOutView.as_view(), name='logout'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path(
        'password_change_done/',
        views.PasswordChangeDoneView.as_view(),
        name='password_change_done',
    ),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm',
    ),
    path(
        'password_reset_done/',
        views.PasswordResetDoneView.as_view(),
        name='password_reset_done',
    ),
    path(
        'password_reset_complete/',
        views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete',
    ),
]
