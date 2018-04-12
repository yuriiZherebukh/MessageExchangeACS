from django.conf.urls import url
from .views import AuthRegister, ObtainJWTView
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    url(r'^login/$', ObtainJWTView.as_view()),
    url(r'^register/$', AuthRegister.as_view()),
]
