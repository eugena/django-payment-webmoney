try:
    from django.conf.urls import url
except ImportError:
    from django.conf.urls.defaults import url

from webmoney.views import result

urlpatterns = [
    url(r'^result/$', result, name='webmoney-result'),
]
