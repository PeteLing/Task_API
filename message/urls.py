from django.conf.urls import url
from message import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

urlpatterns = [
    url(r'^messages/$', views.MessageList.as_view(), name='message-list'),
    url(r'^messages/(?P<pk>[0-9]+)/$', views.MessageDetail.as_view(), name='message-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
