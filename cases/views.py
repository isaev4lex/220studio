from django.shortcuts import render
from .models import *
import contacts.models as contacts
import site_settings.models as settings
import os
import datetime


def cases(request, category_slug=None):
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
        'filters': CaseCategory.objects.all(),
        'main_banners': MainBanner.objects.all(),
        'success_sent': False,
        'page': 'cases',
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
    if category_slug is None:
        data['cases'] = Case.objects.all()
        data['active_filter'] = "all"
    else:
        filtered_cases = []
        active_filter = []
        for case in Case.objects.all():
            if case.category.slug == category_slug:
                filtered_cases.append(case)
        for _filter in CaseCategory.objects.all():
            if _filter.slug == category_slug:
                active_filter.append(_filter)
        data['cases'] = filtered_cases
        data['active_filter'] = active_filter[0]
        

    if not contact_info['name'] or not contact_info['email'] or not contact_info['phone']:
        pass
    else:
        os.system(
            f'bot_engine/main.py --name "{contact_info["name"]}" --phone "{contact_info["phone"]}" '
            f'--email "{contact_info["email"]}" --website "{contact_info["website"]}"')
        data['success_sent'] = True

    return render(request, 'cases/index.html', context=data)
