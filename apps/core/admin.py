from django.contrib import admin
from apps.branche.models import Branche
from apps.daily_sale.models import DailySale
from apps.employee.models import EmployeeUser
from apps.enterprise.models import Enterprise

admin.site.site_header = "Atos Capital"
admin.site.site_title = "Atos Capital"
admin.site.index_title = "Página de administração"

@admin.register(Enterprise)
class EnterpriseAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'cnpj')
    search_fields = ('name', 'email', 'cnpj')

@admin.register(EmployeeUser)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'whatsapp_number', 'enterprise')
    search_fields = ('name', 'whatsapp_number')

@admin.register(Branche)
class BrancheAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'enterprise')
    search_fields = ('name', 'cnpj')

@admin.register(DailySale)
class DailySaleAdmin(admin.ModelAdmin):
    list_display = ('date', 'value', 'goal', 'branche')
    list_filter = ('date', 'branche')