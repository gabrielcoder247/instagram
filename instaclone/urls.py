from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns =[

   
    url(r'^signup/$', views.signup, name='signup'),
     url(r'^profile/(\d+)/$', views.profile, name='profile'),
    url(r'^search/', views.search_results,name='search_results'),
    url(r'^new/image$',views.new_image,name='new_image'),
    url(r'^edit/profile/',views.edit_profile,name='edit_profile'),
    url(r'^$',views.home,name='home_page'),
    url(r'^follow/(\d+)', views.follow, name="follow"),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^likes/(\d+)', views.home, name='likes'),
    # url(r'^comment/(\d+)', views.image, name='comment'),
    
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)