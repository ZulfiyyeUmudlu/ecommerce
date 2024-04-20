from django.contrib import admin
from .models import ContactInfo,Appealing

admin.site.register(ContactInfo)
# admin.site.register(Appealing)

@admin.register(Appealing)
class AppealingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'created_at')
    


