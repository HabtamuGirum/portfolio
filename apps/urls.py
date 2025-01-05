from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('resume/', views.resume, name='resume'),
    path('contact/', views.contact_view, name='contact'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('blog/', views.blog, name='blog'),

    # Dynamic URLs (optional, only if necessary)
    re_path(r'^(?P<random_string>[\w-]+)/resume/$', views.resume, name='resume_random'),
    re_path(r'^(?P<random_string>[\w-]+)/portfolio/$', views.portfolio, name='portfolio_random'),
    re_path(r'^(?P<random_string>[\w-]+)/contact/$', views.contact_view, name='contact_random'),
]
