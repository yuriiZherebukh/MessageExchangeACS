from django.conf.urls import url
from .views import AuthRegister, ObtainJWTView

urlpatterns = [
    url(r'^login/$', ObtainJWTView.as_view()),
    url(r'^register/$', AuthRegister.as_view()),
]
