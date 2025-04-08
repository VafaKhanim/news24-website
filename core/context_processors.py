from django.conf import settings
from .models import Advertisement

def menu_pages(request):
    return {
        'home': getattr(settings, 'HOME_URL', '#'),
        'sports': getattr(settings, 'SPORTS_URL', '#'),
        'tech': getattr(settings, 'TECH_URL', '#'),
        'fashion': getattr(settings, 'FASHION_URL', '#'),
        'business': getattr(settings, 'BUSINESS_URL', '#'),
        'politics': getattr(settings, 'POLITICS_URL', '#'),
        'contact': getattr(settings, 'CONTACT_URL', '#'),
    }

def social_media(request):
    return {
        'twitter': getattr(settings, 'TWITTER_URL', '#'),
        'facebook': getattr(settings, 'FACEBOOK_URL', '#'),
        'linkedin': getattr(settings, 'LINKEDIN_URL', '#'),
        'instagram': getattr(settings, 'INSTAGRAM_URL', '#'),
        'youtube': getattr(settings, 'YOUTUBE_URL', "#")
    }

def categories_pages(request):
    return {
        'entertainment' : getattr(settings, 'ENTERTAINMENT_URL', '#'),
        'national': getattr(settings, 'NATIONAL_URL', '#'),
        'international': getattr(settings, 'INTERNATIONAL_URL', '#'),
        'economics': getattr(settings, 'ECONOMICS_URL', '#'),
        'trades': getattr(settings, 'TRADES_URL', '#')
    }


def ads_processor(request):
    main_ad = Advertisement.objects.filter(columns='main').order_by('-id').first()
    other_ads = Advertisement.objects.filter(columns='others').order_by('-id')[:2]
    return {
        'main_ad': main_ad,
        'other_ads': other_ads
    }


def contact_ways(request):
    return {
        'call' : getattr(settings, 'CALL_URL', '#'),
        'mail' : getattr(settings, 'MAIL_URL', '#'),
        'location': getattr(settings, 'LOCATION_URL', '#')
    }
