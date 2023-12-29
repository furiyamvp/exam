from django.urls import path
from pages.views import *

app_name = "pages"

urlpatterns = [
    path("", home_page_view, name="home"),
    path("booking/", booking_view, name="booking")
]
