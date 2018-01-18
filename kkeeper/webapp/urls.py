from django.conf.urls import url
from webapp import views
from django.conf.urls import include


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^About/$', views.AboutPageView.as_view(), name='about'),
    url(r'^Products/$', views.ProductsPageView.as_view(), name='products'),
    url(r'^Careers/$', views.CareersPageView.as_view(), name='careers'),
    url(r'^Terms/$', views.TermsPageView.as_view(), name='terms'),
    url(r'^Privacy/$', views.PrivacyPageView.as_view(), name='privacy'),
    url(r'^blog/', include('andablog.urls', namespace='andablog')),


#email
    url(r'^email/$', views.email, name='email'),
    url(r'^thanks/$', views.thanks, name='thanks'),

#blog
    # url(r'^$', views.posts, name='posts'),
    # url(r'^$', views.comments, name='comments')
]
