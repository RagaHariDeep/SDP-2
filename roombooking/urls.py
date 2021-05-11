from django.urls import path
from . import views
urlpatterns = [
    path("searchrooms/",views.searchrooms,name="searchrooms"),
    path("bookroom/<str:roomno>/<str:roomtype>/<str:price>/",views.bookroom,name="bookroom"),
    path("cancelroom/<str:email>/<str:roomno>/",views.cancelroom,name="cancelroom"),
]