from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'website'

urlpatterns = [
    url(r"post/$", views.PostView.as_view(), name="post"),
    url(r"member/$", views.MemberView.as_view(), name='member'),
    url(r"logo/$", views.LogoView.as_view(), name='logo'),
    url(r"description/$", views.DescriptionView.as_view(), name='description'),
    url(r"contact/$", views.ContactView.as_view(), name='contact'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)