from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
from receiver.views import HomeView, IntelView, UpoView

urlpatterns = [
    url(r'^intel/?$', csrf_exempt(IntelView.as_view()), name='intel_dump'),
    url(r'^upo', UpoView.as_view(), name='upoguide'),
    url(r'^', HomeView.as_view(), name='home'),
]
