"""
This module contains routes to specific app from the project
"""

from django.conf.urls import url, include

urlpatterns = [

    url(r'^api/v1/auth/', include('authentication.urls')),
    url(r'^api/v1/institute/', include('institute.urls')),
    url(r'^api/v1/department/', include('department.urls')),
]
