from django.conf.urls import url

from . import views

urlpatterns = [url(r'^$', views.questions, name="questions"),
                url(r'^(?P<question_id>[0-9]+)/$', views.questiondetail, name="questiondetail"),
               ]