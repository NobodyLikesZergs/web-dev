from django.conf.urls import url
from .views import QuestionList, QuestionView, QuestionCreate, QuestionUpdate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', QuestionView.as_view(), name="question_view"),
    url(r'^$', QuestionList.as_view(), name='question_list'),
    url(r'^create/$', login_required(QuestionCreate.as_view()),
        name="question_create"),
    url(r'^(?P<pk>\d+)/update/$', QuestionUpdate.as_view(),
        name="question_update"),
]
