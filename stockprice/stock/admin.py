from django.contrib import admin

# Register your models here.
from stock.models import DailyPrice

admin.site.register(DailyPrice)