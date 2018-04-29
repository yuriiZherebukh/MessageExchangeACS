from .views import UserProfileView

from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', UserProfileView.as_view()),
    url(r'^(?P<profile_id>\d+)/$', UserProfileView.as_view()),
]

