from django.conf.urls import url
from .views import ListSongsView, CreateSongsView, login


urlpatterns = [

url(r'^login/$', login, name='auth'),
url(r'^songs/$', CreateSongsView.as_view(), name='songs-add'),
url(r'^songs/(?P<pk>[0-9]+)/$', ListSongsView.as_view(), name="songs-all"),

]
