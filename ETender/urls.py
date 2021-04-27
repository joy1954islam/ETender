"""ETender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from holder import views as holder

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('super/admin/', include('SuperAdmin.urls')),
    path('government/employee/', include('government_employee.urls')),

    path('', holder.home_tender_list, name='index'),
    path('apply/tender/<int:tender_id>/', holder.apply_tender_create, name='apply_tender_create'),
    path('apply/tender/holder/list/', holder.list_of_apply_tender, name='list_of_apply_tender'),
    path('apply/tender/holder/short/list/<int:tender_id>/', holder.holder_list_of_holder_short_list,
         name='holder_list_of_holder_short_list'),
    path('apply/tender/holder/winner/list/<int:tender_id>/', holder.holder_winner_holder_list,
         name='holder_winner_holder_list'),
    path('my/tender/list/', holder.user_winner_holder_list,
         name='user_winner_holder_list'),

    path('about/', holder.about, name='about'),
    path('service/', holder.service, name='service'),
    path('all_tender_notice/', holder.all_tender_notice, name='all_tender_notice'),
    path('tender_chart/', holder.tender_chart, name='tender_chart'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)