from django.conf.urls import url
from django.contrib import admin
from eventex.core.views import home
from eventex.subscriptions.views import subscribe, detail

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^inscricao/$', subscribe, name='subscribe'),
    url(r'^inscricao/(\d+)/$', detail , name='detail'),
    url(r'^admin/', admin.site.urls),
]
