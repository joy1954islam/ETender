from django.urls import path

from SuperAdmin import views

urlpatterns = [
    path('home/', views.SuperAdminHome, name='SuperAdminHome'),
    path('profile/',views.SuperAdminProfile, name='SuperAdminProfile'),
    path('GovtSignUpView/',views.GovtSignUpView.as_view(), name='GovtSignUpView'),

    path('ministry/', views.ministry_list, name='ministry_list'),
    path('ministry/create/', views.ministry_create, name='ministry_create'),
    path('<int:pk>/ministry/update/', views.ministry_update, name='ministry_update'),
    path('<int:pk>/ministry/delete/', views.ministry_delete, name='ministry_delete'),

    path('employee/', views.employee_list, name='employee_list'),
    path('employee/create/', views.GovtSignUpView.as_view(), name='employee_create'),
    path('<int:pk>/employee/update/', views.employee_update, name='employee_update'),
    path('<int:pk>/employee/delete/', views.employee_delete, name='employee_delete'),
    path('<int:pk>/employee/view/', views.employee_view, name='employee_view'),

    path('change/password/', views.ChangePasswordView.as_view(), name='SuperAdmin_change_password'),
    path('change/email/', views.ChangeEmailView.as_view(), name='SuperAdmin_change_email'),
    path('change/email/<code>/', views.ChangeEmailActivateView.as_view(), name='change_email_activation'),

    path('holder/', views.holder_registration_list, name='holder_registration_list'),
    path('holder/registration/details/<int:holder_id>/', views.holder_registration_details,
         name='holder_registration_details'),
    path('holder/registration/approve/<int:holder_id>/', views.holder_registration_approved,
         name='holder_registration_approved'),
]
