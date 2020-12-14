
from django.urls import path
from . import views
app_name = 'stock'
urlpatterns = [
    path('',views.home),
    path('ajax/',views.home_ajax, name="home_ajax"),
    path('update_chart/',views.update_chart, name="update_chart"),
    path('api/symbol=<symbol>',views.symbolData.as_view(),name='onesymbol'),
]
