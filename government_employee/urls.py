from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', government_employee_home, name='government_employee_home'),

    path('tender/upload/', tender_upload_list, name='tender_upload_list'),
    path('tender/upload/create/', tender_upload_create, name='tender_upload_create'),
    path('tender/upload/update/<int:tender_id>/', tender_upload_update, name='tender_upload_update'),
    path('tender/upload/delete/<int:tender_id>/', tender_upload_delete, name='tender_upload_delete'),
    path('tender/upload/details/<int:tender_id>/', tender_upload_details, name='tender_upload_details'),

    path('apply/tender/list/<int:tender_id>/', list_of_apply_tender, name='list_of_apply_tender'),
    path('apply/tender/holder/status/change/<int:tender_id>/', change_status_of_apply_tender_holder,
         name='change_status_of_apply_tender_holder'),
    path('apply/tender/holder/details/<int:tender_id>/', apply_tender_holder_details,
         name='apply_tender_holder_details'),
    path('apply/tender/holder/short/list/<int:tender_id>/<int:user_id>/', short_list_of_apply_tender_holder,
         name='short_list_of_apply_tender_holder'),
    path('apply/tender/holder/short/list/<int:tender_id>/', list_of_holder_short_list,
         name='list_of_holder_short_list'),
    path('apply/tender/holder/winner/create/<int:tender_id>/', winner_holder,
         name='winner_holder'),
    path('apply/tender/holder/winner/list/<int:tender_id>/', winner_holder_list,
         name='winner_holder_list'),

    path('change/profile/', government_employee__profile, name='government_change_profile'),
    path('change/password/', ChangePasswordView.as_view(), name='government_change_password'),
    path('change/email/', ChangeEmailView.as_view(), name='government_change_email'),
    path('change/email/<code>/', ChangeEmailActivateView.as_view(), name='government_change_email_activation'),

    path('tender_notice_list/<int:tender_id>/', tender_notice_list, name='tender_notice_list'),
    path('tender_notice_create/<int:tender_id>/', tender_notice_create, name='tender_notice_create'),
    path('tender_notice_update/<int:tender_notice_id>/', tender_notice_update, name='tender_notice_update'),
    path('tender_notice_delete/<int:tender_notice_id>/', tender_notice_delete, name='tender_notice_delete'),


    path('meanual_winner_holder/<int:tender_id>/<int:user_id>/', meanual_winner_holder, name='meanual_winner_holder'),

]
