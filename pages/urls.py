from django.urls import path
from .views import (
    index, 
    citylab, 
    contact, 
    about,
    luic,
    portfolio,
    mcf,
    news)

urlpatterns = [
    path('', index, name='home'),
    path('citylabs/', citylab, name='citylab'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('lagos-urban-innovation-challenge/', luic, name='luic'),
    path('portfolio/', portfolio, name='portfolio'),
    path('mcf/', mcf, name='mcf'),
    path('news/', news, name='news'),

]
