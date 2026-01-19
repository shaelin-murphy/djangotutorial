from django.contrib import admin
from .models import Client, IntakeRecord


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'city', 'household_size', 
                    'monthly_income', 'eligibility_status', 'intake_date', 'visit_count']
    list_filter = ['eligibility_status', 'city', 'state', 'intake_date']
    search_fields = ['first_name', 'last_name', 'city', 'zip_code', 'phone', 'email']
    readonly_fields = ['created_at', 'updated_at', 'visit_count']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'date_of_birth', 'phone', 'email')
        }),
        ('Address', {
            'fields': ('street_address', 'city', 'state', 'zip_code')
        }),
        ('Household Information', {
            'fields': ('household_size', 'monthly_income')
        }),
        ('Eligibility', {
            'fields': ('eligibility_status', 'eligibility_notes')
        }),
        ('Intake Information', {
            'fields': ('intake_date', 'intake_staff', 'special_notes')
        }),
        ('Tracking', {
            'fields': ('last_visit_date', 'visit_count', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(IntakeRecord)
class IntakeRecordAdmin(admin.ModelAdmin):
    list_display = ['client', 'visit_date', 'staff_member', 'created_at']
    list_filter = ['visit_date', 'staff_member']
    search_fields = ['client__first_name', 'client__last_name', 'notes']
    date_hierarchy = 'visit_date'
