from .views import MeetingView

from django.conf.urls import url

urlpatterns = [
    url(r'^$', MeetingView.as_view()),
    url(r'owner/$', MeetingView.as_view(), {'owner': True}),
    url(r'^(?P<meeting_id>\d+)/$', MeetingView.as_view()),
]
