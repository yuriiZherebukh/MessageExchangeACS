from .views import GroupView

from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', GroupView.as_view()),
    url(r'^(?P<group_id>\d+)/$', GroupView.as_view()),
]
