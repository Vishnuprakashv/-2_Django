from django.contrib import admin
from . models import Emp

# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    # Show in table format inside admin pannel
    list_display = ('name','dept',)
    # Edit inside admin pannel
    list_edittable = ('name',)
    # Search data inside admin panel
    search_fields = ('name',)
#
admin.site.register(Emp,EmpAdmin)

