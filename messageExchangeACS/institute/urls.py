from .views import InstituteView

from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', InstituteView.as_view()),
    url(r'^(?P<institute_id>\d+)/$', InstituteView.as_view()),
    url(r'^(?P<institute_id>\d+)/department/', include('department.urls')),
    # url(r'^(?P<institute_id>\d+)/department/', include('department.urls')),
    #url(r'^(?P<institute_id>\d+)/profile/', include('profile.urls')),
]
