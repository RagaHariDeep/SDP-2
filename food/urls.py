from django.urls import path
from . import views
urlpatterns = [
    path("bookdinein/",views.bookdinein,name="bookdinein"),
    path("canceldinein/<str:email>/<int:tableno>/",views.canceldinein,name="canceldinein"),
]