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

]
