from django.conf.urls import url
from . import views
from .views import emailView, successView
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog.html', views.blog_page, name='blog-version-one'),
    url(r'^tour/(?P<id>\d+)/$', views.tour_page, name='tour_page'),
    url(r'^post/(?P<id>\d+)/', views.post_detail, name='post_detail'),
    url(r'^contact.html', views.contact, name='contact')


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





