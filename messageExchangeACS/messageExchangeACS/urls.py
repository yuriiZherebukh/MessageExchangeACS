"""
This module contains routes to specific app from the project
"""

from django.conf.urls import url, include

urlpatterns = [

    url(r'^api/v1/auth/', include('authentication.urls')),
    url(r'^api/v1/institute/', include('institute.urls')),
    url(r'^api/v1/department/', include('department.urls')),
    url(r'^api/v1/message/', include('message.urls')),
    url(r'^api/v1/classroom/', include('classroom.urls')),
    url(r'^api/v1/meeting/', include('meeting.urls')),
    url(r'^api/v1/profile/', include('user_profile.urls')),
    url(r'.*', include('home.urls')),
]
