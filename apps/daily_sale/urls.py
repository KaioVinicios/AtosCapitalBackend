from django.contrib import admin
from django.urls import path, include
from apps.daily_sale.views import show_daily_sales_by_date

urlpatterns = [
    path(
        "require_daily_sales/<str:enterprise_url>/",
        show_daily_sales_by_date,
        name="show_daily_sales_by_date",
    )
]
