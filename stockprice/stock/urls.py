
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home),
    path('api/symbol=<symbol>',views.symbolData.as_view(),name='onesymbol'),
]