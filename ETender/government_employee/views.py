from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import *
import random
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    LogoutView as BaseLogoutView, PasswordChangeView as BasePasswordChangeView,
)
from django.contrib.auth import login
from accounts.models import Activation
from django.utils.crypto import get_random_string
from django.views.generic import View, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.utils import (
    send_activation_email, send_reset_password_email, send_forgotten_username_email, send_activation_change_email,
)
from accounts.forms import (
    SignInViaUsernameForm, SignInViaEmailForm, SignInViaEmailOrUsernameForm, SignUpForm,
    RestorePasswordForm, RestorePasswordViaEmailOrUsernameForm, RemindUsernameForm,
    ResendActivationCodeForm, ResendActivationCodeViaEmailForm, ChangeProfileForm, ChangeEmailForm
)
from django.contrib import messages
from holder.models import ApplyTender
from .forms import *
from django.contrib.auth import get_user_model

from accounts.forms import UserUpdateForm

User = get_user_model()


def government_employee_home(request):
    return render(request, 'government_employee/Home.html')


def register_holder_list(request):
    holder = Holder.objects.all()
    context = {
        'holder': holder
    }
    return render(request, '', context=context)


def tender_upload_list(request):
    tender = TenderUpload.objects.filter(username=request.user)
    context = {
        'tender': tender
    }
    return render(request, 'government_employee/TenderUpload/tender_list.html', context=context)


def tender_upload_create(request):
    if request.method == "POST":
        form = TenderUploadForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            t = form.save(commit=False)
            t.username = request.user
            t.save()
            return redirect(reverse('tender_upload_list'))
        context = {
            'form': form
        }
        return render(request, 'government_employee/TenderUpload/tender_create.html', context=context)
    if request.method == "GET":
        form = TenderUploadForm()
        context = {
            'form': form
        }
        return render(request, 'government_employee/TenderUpload/tender_create.html', context=context)


def tender_upload_update(request, tender_id):
    tender = TenderUpload.objects.get(id=tender_id)
    if request.method == "POST":
        form = TenderUploadForm(request.POST or None, request.FILES or None, instance=tender)
        if form.is_valid():
            form.save()
            return redirect(reverse('tender_upload_list'))
        context = {
                'form': form
            }
        return render(request, 'government_employee/TenderUpload/tender_upload.html', context=context)
    if request.method == "GET":
        form = TenderUploadForm(instance=tender)
        context = {
            'form': form
        }
        return render(request, 'government_employee/TenderUpload/tender_upload.html', context=context)


def tender_upload_delete(request, tender_id):
    tender = TenderUpload.objects.get(id=tender_id)
    if request.method == "POST":
        tender.delete()
        context = {
            'tender': tender
        }
        return render(request, 'government_employee/TenderUpload/tender_delete.html', context=context)
    if request.method == "GET":
        context = {
            'tender': tender
        }
        return render(request, 'government_employee/TenderUpload/tender_delete.html', context=context)


def tender_upload_details(request, tender_id):
    tender = TenderUpload.objects.get(id=tender_id)
    context = {
        'tender': tender
    }
    return render(request, 'government_employee/TenderUpload/tender_details.html', context=context)


def list_of_apply_tender(request, tender_id):
    apply_tender = ApplyTender.objects.filter(tender=tender_id)
    context = {
        'apply_tender': apply_tender,
    }
    return render(request, 'government_employee/ApplyTender/apply_tender_list.html', context=context)


def apply_tender_holder_details(request, tender_id):
    apply_tender = ApplyTender.objects.get(id=tender_id)
    context = {
        'apply_tender': apply_tender
    }
    return render(request, 'government_employee/ApplyTender/apply_tender_details.html', context=context)


def change_status_of_apply_tender_holder(request, tender_id):
    apply_tender = ApplyTender.objects.get(id=tender_id)
    tender = TenderUpload.objects.get(title=apply_tender)
    form = ApplyTenderHolderUpdateForm(instance=apply_tender)
    if request.method == "POST":
        form = ApplyTenderHolderUpdateForm(request.POST or None, instance=apply_tender)
        if form.is_valid():
            form.save()
            return redirect('list_of_apply_tender', tender.id)
    if request.method == "GET":
        context = {
            'form': form
        }
        return render(request, 'government_employee/ApplyTender/apply_tender_status_change.html', context=context)


def short_list_of_apply_tender_holder(request, tender_id, user_id):
    apply_tender = ApplyTender.objects.get(id=tender_id)
    tender = TenderUpload.objects.get(title=apply_tender)
    user = User.objects.get(id=user_id)
    short_list = ApplyTenderHolderShortList()
    short_list.tender = apply_tender
    short_list.username = user
    exists_user = ApplyTenderHolderShortList.objects.filter(tender=apply_tender, username=user)
    if exists_user.exists():
        messages.add_message(request, messages.INFO, 'This User Is Already Short Listed')
        return redirect('list_of_apply_tender', tender.id)
    else:
        short_list.save()
        return redirect('list_of_apply_tender', tender.id)


def list_of_holder_short_list(request, tender_id):
    short_list = ApplyTenderHolderShortList.objects.filter(tender_id=tender_id)
    context = {
        'short_list': short_list
    }
    return render(request, 'government_employee/ApplyTender/apply_tender_holder_short_list.html', context=context)


def winner_holder(request, tender_id):
    holder_short_list = ApplyTenderHolderShortList.objects.filter(tender=tender_id)
    w = WinnerHolder.objects.filter(tender=tender_id)
    if w.exists():
        messages.add_message(request, messages.INFO, 'This Tender Is Already Winner Listed')
        return redirect('winner_holder_list', tender_id)
    else:
        winner = random.choice(holder_short_list)
        winner_tender = winner.tender
        winner_username = winner.username
        winner_holder = WinnerHolder()
        winner_holder.tender = winner_tender
        winner_holder.username = winner_username
        winner_holder.save()
        return redirect('winner_holder_list', tender_id)


def winner_holder_list(request, tender_id):
    winner_holder = WinnerHolder.objects.filter(tender=tender_id)
    context = {
        'winner_holder': winner_holder
    }
    return render(request, 'government_employee/ApplyTender/wiiner_holder_list.html', context=context)


def government_employee__profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST or None, request.FILES or None, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('government_change_profile')
    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form
    }
    return render(request, 'government_employee/profile/GovernmentEmployeeProfile.html', context)


class ChangeEmailView(LoginRequiredMixin, FormView):
    template_name = 'government_employee/profile/change_email.html'
    form_class = ChangeEmailForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial['email'] = self.request.user.email
        return initial

    def form_valid(self, form):
        user = self.request.user
        email = form.cleaned_data['email']

        if settings.ENABLE_ACTIVATION_AFTER_EMAIL_CHANGE:
            code = get_random_string(20)

            act = Activation()
            act.code = code
            act.user = user
            act.email = email
            act.save()

            send_activation_change_email(self.request, email, code)

            messages.success(self.request, f'To complete the change of email address, click on the link sent to it.')
        else:
            user.email = email
            user.save()

            messages.success(self.request, f'Email successfully changed.')

        return redirect('government_change_email')


class ChangeEmailActivateView(View):
    @staticmethod
    def get(request, code):
        act = get_object_or_404(Activation, code=code)

        # Change the email
        user = act.user
        user.email = act.email
        user.save()

        # Remove the activation record
        act.delete()

        messages.success(request, f'You have successfully changed your email!')

        return redirect('government_change_email')


class ChangePasswordView(BasePasswordChangeView):
    template_name = 'government_employee/profile/change_password.html'

    def form_valid(self, form):
        # Change the password
        user = form.save()

        # Re-authentication
        login(self.request, user)

        messages.success(self.request, f'Your password was changed.')

        return redirect('government_change_password')
