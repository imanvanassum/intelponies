from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from receiver.views import HomeView, IntelView

urlpatterns = [
    url(r'^intel/?$', csrf_exempt(IntelView.as_view()), name='intel_dump'),
    url(r'^', HomeView.as_view(), name='home'),
]
