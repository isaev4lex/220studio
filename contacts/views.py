from django.shortcuts import render
from .models import *
import partners.models as partners
import site_settings.models as settings
import os
import datetime


def contacts(request):
    contact_info = {
        'name': request.GET.get('name'),
        'email': request.GET.get('email'),
        'phone': request.GET.get('phone'),
        'website': request.GET.get('website'),
    }
    data = {
        'meta': MetaTags.objects.all(),
        'favicons': settings.Favicon.objects.all(),
        'head_tags': settings.HeadTags.objects.all(),
        'success_sent': False,
        'page': 'contacts',
        'contact_info': {
            'phones': Phone.objects.all(),
            'emails': Email.objects.all(),
            'addresses': Address.objects.all()
        },
        'year': str(datetime.datetime.now().year),
        'footer_info': {
            'instagram': Instagram.objects.all(),
            'facebook': Facebook.objects.all(),
            'telegram': Telegram.objects.all(),
            'tik-tok': TikTok.objects.all(),
        }
    }
    if not contact_info['name'] or not contact_info['email'] or not contact_info['phone']:
        pass
    else:
        os.system(
            f'bot_engine/main.py --name "{contact_info["name"]}" --phone "{contact_info["phone"]}" '
            f'--email "{contact_info["email"]}" --website "{contact_info["website"]}"')
        data['success_sent'] = True

    return render(request, 'contacts/index.html', context=data)
