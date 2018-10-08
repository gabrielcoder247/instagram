from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[
   
    url(r'^$',views.home,name='home_page'),
    # url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name='pastNews'),
    url(r'^profile/',views.profile,name ='profile_page'),
    url(r'^search/', views.search_results,name='search_results'),
    url(r'^new/profile$', views.new_profile, name='new_profile') 
    url(r'^new/image$',views.new_image,name='new_image'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)