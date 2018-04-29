from .views import ClassroomView

from django.conf.urls import url

urlpatterns = [
    url(r'^$', ClassroomView.as_view()),
    url(r'^(?P<classroom_id>\d+)/$', ClassroomView.as_view()),
]
