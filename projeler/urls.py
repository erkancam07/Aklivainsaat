from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),  # ← bu olmalı
    path("index",views.index,name="index"),
    path("kurumsal",views.kurumsal,name="kurumsal"),
    path("projeler",views.projeler,name="projeler"),
    path("haberler",views.haberler,name="haberler"),
    path("yatirim",views.yatirim,name="yatirim"),
    path("iletisim",views.iletisim,name="iletisim"),
    
    
]

