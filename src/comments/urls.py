from django.conf.urls import url
from .views import CommentUpdate

urlpatterns = [
    url(r'^(?P<pk>\d+)/update/$', CommentUpdate.as_view(),
        name="comment_update"),
]
