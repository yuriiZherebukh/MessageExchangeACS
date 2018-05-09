from django.conf.urls import url
from .views import AuthRegister, ObtainJWTView, UserListView

urlpatterns = [
    url(r'^login/$', ObtainJWTView.as_view()),
    url(r'^register/$', AuthRegister.as_view()),
    url(r'^user/', UserListView.as_view()),
    url(r'^user/(?P<user_id>\d+)/$', UserListView.as_view()),
]
