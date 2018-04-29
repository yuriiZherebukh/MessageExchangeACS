from .views import MessageView

from django.conf.urls import url

urlpatterns = [
    url(r'^$', MessageView.as_view()),
    url(r'^(?P<message_id>\d+)/$', MessageView.as_view()),
]
