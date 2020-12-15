
from django.urls import path
from . import views
app_name = 'stock'
urlpatterns = [
    path('',views.home),
    path('ajax/',views.home_ajax, name="home_ajax"),
    path('api/symbol=<symbol>',views.symbolData.as_view(),name='onesymbol'),
]
