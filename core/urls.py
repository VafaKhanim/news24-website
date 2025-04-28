from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page, name ='home_page'),
    path('contact/', views.contact_page, name ='contact_page'),
    path('sports/', views.sports_page, name ='sports_page'),
    path('tech/', views.tech_page, name ='tech_page'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('business/', views.business_page, name ='business_page'),
    path('entertainment/', views.entertainment_page, name ='entertainment_page'),
    path('politics/', views.politics_page, name ='politics_page'),
    path('fashion/', views.fashion_page, name ='fashion_page'),
    path('trades/', views.trades_page, name ='trades_page'),
    path('national/', views.national_page, name ='national_page'),
    path('international/', views.international_page, name ='international_page'),
    path('economics/', views.economics_page, name ='economics_page'),
    path('latest/', views.latest_news, name ='latest_news'),
    path('popular/', views.popular_news, name ='popular_news'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path ('search/', views.search_view, name = 'search_view')

    ]