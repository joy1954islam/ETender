from django.contrib.auth import get_user_model
User = get_user_model()


def get_all_notification(request):
    holder_user = User.objects.exclude(is_government_employee=True).exclude(is_superuser=True).exclude(is_tender_holder=True)
    context = {
        'holder_user': holder_user
    }
    return context

