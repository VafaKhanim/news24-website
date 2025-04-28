from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm, SubscribeForm
from .models import Contact, News, NewsCategory, Advertisement, Subscribe
from django.db.models import Q


def home_page(request):
    main_news = News.objects.filter(featured_type='main').order_by('-pub_date').first()
    side_news = News.objects.filter(featured_type='side').order_by('-pub_date')[:4]

    sports_news = News.objects.filter(categories__name="Sports").order_by('-pub_date')[:4]
    tech_news = News.objects.filter(categories__name="Tech").order_by('-pub_date')[:4]
    business_news = News.objects.filter(categories__name="Business").order_by('-pub_date')[:4]
    entertainment_news = News.objects.filter(categories__name="Entertainment").order_by('-pub_date')[:4]

    popular_news_list = News.objects.order_by('-view_count')[:6]
    most_popular_news = popular_news_list[0]
    other_popular_news = popular_news_list[1:]

    latest_news_list = News.objects.order_by('-pub_date')[:6]
    latest_news = latest_news_list[0]
    other_latest_news = latest_news_list[1:]


    context = {
        'main_news': main_news,
        'side_news': side_news,
        'sports_news': sports_news,
        'tech_news': tech_news,
        'business_news': business_news,
        'entertainment_news': entertainment_news,
        'most_popular_news': most_popular_news,
        'other_popular_news': other_popular_news,
        'latest_news': latest_news,
        'other_latest_news': other_latest_news,
    }



    return render(request, 'index.html', context)



def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            message = form.cleaned_data.get('message')

            Contact.objects.create(
                name = name,
                email = email,
                subject = subject,
                message = message
            )

    return render(request, 'contact.html')



def sports_page(request):
    category = NewsCategory.objects.get(name="Sports")
    sports_news = News.objects.filter(categories=category)
    context = {

        'page_name': 'Sports News',
        'newses': sports_news
    }
    return render(request, 'news_page.html', context)



def tech_page(request):
    category = NewsCategory.objects.get(name="Tech")
    tech_news = News.objects.filter(categories=category)
    context = {
        'page_name': 'Tech News',
        'newses': tech_news
    }
    return render(request, 'news_page.html', context)





def news_detail(request, news_id):
    news = get_object_or_404(News, id=news_id)
    news.view_count += 1
    news.save()
    context = {
        'news': news,
    }
    return render(request, 'news_detail.html', context)




def business_page(request):
    category = NewsCategory.objects.get(name = "Business")
    business_news = News.objects.filter(categories = category)
    context = {
        'page_name': 'Business News',
        'newses': business_news
    }
    return render(request, 'news_page.html', context)


def entertainment_page(request):
    category = NewsCategory.objects.get(name = "Entertainment")
    entertainment_news = News.objects.filter(categories = category)
    context = {
        'page_name': 'Entertainment News',
        'newses': entertainment_news
    }
    return render(request, 'news_page.html', context)


def fashion_page(request):
    category = NewsCategory.objects.get(name = "Fashion")
    fashion_news = News.objects.filter(categories = category)
    context = {
        'page_name': 'Fashion News',
        'newses': fashion_news
    }
    return render(request, 'news_page.html', context)


def politics_page(request):
    category = NewsCategory.objects.get(name = "Politics")
    politics_news = News.objects.filter(categories = category)
    context = {
        'page_name': 'Politics News',
        'newses': politics_news
    }
    return render(request, 'news_page.html', context)


def trades_page(request):
    category = NewsCategory.objects.get(name = "Trades")
    politics_news = News.objects.filter(categories = category)
    context = {
        'page_name': 'Politics News',
        'newses': politics_news
    }
    return render(request, 'news_page.html', context)


def economics_page(request):
    category = NewsCategory.objects.get(name = "Economics")
    economics_news = News.objects.filter(categories = category)
    context = {
        'page_name': 'Economics News',
        'newses': economics_news
    }
    return render(request, 'news_page.html', context)


def national_page(request):
    category = NewsCategory.objects.get(name = "National")
    national_news = News.objects.filter(categories = category)
    context = {
        'page_name': 'National News',
        'newses': national_news
    }
    return render(request, 'news_page.html', context)


def international_page(request):
    category = NewsCategory.objects.get(name = "International")
    international_news = News.objects.filter(categories = category)
    context = {
        'page_name': 'International News',
        'newses': international_news
    }
    return render(request, 'news_page.html', context)


def latest_news(request):
    latest_news_list = News.objects.order_by('-pub_date')[:12]
    context = {
        'page_name': 'Latest News',
        'newses': latest_news_list
    }
    return render(request, 'news_page.html', context)


def popular_news(request):
    popular_news = News.objects.order_by('-view_count')[:12]
    context = {
        'page_name': 'Popular News',
        'newses': popular_news
    }
    return render(request, 'news_page.html', context)



def subscribe(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')

            Subscribe.objects.create(
                email = email,
            )

    return redirect(request.META.get("HTTP_REFERER", "/"))


def search_view(request):
    key_data = request.GET.get('key', False)
    if key_data:
        posts = News.objects.filter(Q(title__icontains = key_data) | Q(content__icontains = key_data))

        context = {
            'page_name': 'Results',
            'newses' : posts,

        }
        return render(request, 'news_page.html', context)