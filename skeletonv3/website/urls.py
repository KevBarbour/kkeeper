from django.conf.urls import url
from website import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^About/$', views.AboutPageView.as_view(), name='about'),
    url(r'^Products/$', views.ProductsPageView.as_view(), name='products'),
    url(r'^Careers/$', views.CareersPageView.as_view(), name='careers'),
    url(r'^Terms/$', views.TermsPageView.as_view(), name='terms'),
    url(r'^Privacy/$', views.PrivacyPageView.as_view(), name='privacy'),

    url(r'^email/$', views.email, name='email'),
    url(r'^thanks/$', views.thanks, name='thanks'),
]
