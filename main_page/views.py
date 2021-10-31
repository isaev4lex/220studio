from django.shortcuts import render
from . import models
import contacts.models as contacts
import site_settings.models as settings
import os
import datetime


def home(request):
    contact_info = {
        'name': request.GET.get('name'),
        'email': request.GET.get('email'),
        'phone': request.GET.get('phone'),
        'website': request.GET.get('website'),
    }
    data = {
        'meta': models.MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'main_banners': models.MainBanner.objects.all(),
        'cases': models.CaseImages.objects.all(),
        # 'work_result': models.Counter.objects.all(),
        'services': models.Services.objects.all(),
        'work_steps': models.WorkSteps.objects.all(),
        'success_sent': False,
        'page': 'home',
        'contact_info': {
            'phones': contacts.Phone.objects.all(),
            'emails': contacts.Email.objects.all(),
            'addresses': contacts.Address.objects.all()
        },
        'year': str(datetime.datetime.now().year),
        'footer_info': {
            'instagram': contacts.Instagram.objects.all(),
            'facebook': contacts.Facebook.objects.all(),
            'telegram': contacts.Telegram.objects.all(),
            'tik-tok': contacts.TikTok.objects.all(),
        }
    }
    if not contact_info['name'] or not contact_info['email'] or not contact_info['phone']:
        pass
    else:
        os.system(
            f'bot_engine/main.py --name "{contact_info["name"]}" --phone "{contact_info["phone"]}" '
            f'--email "{contact_info["email"]}" --website "{contact_info["website"]}"')
        data['success_sent'] = True

    return render(request, 'main_page/index.html', context=data)
