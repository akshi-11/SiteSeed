from django.conf.urls import url
from .views import UserList, UserDetail, signup


urlpatterns = [
    url(r'signup$', signup, name="signup"),
    url(r'users$', UserList.as_view(), name="user_list"),
    url(r'user/(?P<pk>[0-9]+)/', UserDetail.as_view()),
]
