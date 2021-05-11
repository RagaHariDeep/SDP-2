from django.urls import path
from . import views
urlpatterns = [
    path("adminhomepage/",views.adminhomepage,name="adminhomepage"),
    path("adminaddroom/",views.adminaddroom,name="adminaddroom"),
    path("adminviewrooms/",views.adminviewrooms,name="adminviewrooms"),
    path("adminupdateroom/<str:roomno>/",views.adminupdateroom,name="adminupdateroom"),
    path("admindeleteroom/<str:roomno>/",views.admindeleteroom,name="admindeleteroom"),
    path("adminaddtable/",views.adminaddtable,name="adminaddtable"),
    path("adminviewtables/",views.adminviewtables,name="adminviewtables"),
    path("adminupdatetable/<str:tableno>/",views.adminupdatetable,name="adminupdatetable"),
    path("admindeletetable/<str:tableno>/",views.admindeletetable,name="admindeletetable"),
    path('chartsdata/', views.chartsdata, name='chartsdata'),
]