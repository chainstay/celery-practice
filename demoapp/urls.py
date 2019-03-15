from django.conf.urls import url
from .views import add_view, get_result

urlpatterns = [
    url('add', add_view),
    url('result', get_result),
]
