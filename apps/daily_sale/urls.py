from django.contrib import admin
from django.urls import path, include
from apps.daily_sale.views import require_all_daily_sales, require_daily_sales_by_date

urlpatterns = [
    path(
        "require_daily_sales/",
        require_all_daily_sales,
        name="require_all_daily_sales"
    ),
    path(
        "require_daily_sales_by_date/<str:date>/",
        require_daily_sales_by_date, 
        name="require_daily_sales")
]
