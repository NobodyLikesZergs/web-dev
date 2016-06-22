from django.conf.urls import url
from .views import RegisterFormView
from .views import LoginFormView
from django.contrib.auth.views import logout

urlpatterns = [
    url(r'^login/$', LoginFormView.as_view(), name='login'),
    url(r'^logout/$', logout, {'next_page': '/'},
        name='logout'),
    url(r'signup/$', RegisterFormView.as_view(), name='user_create'),
]
