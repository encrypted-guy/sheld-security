from django.contrib import admin

# Register your models here.
from .models import Contact, InquiryModal

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email'
    )
class InquiryModalAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'email',
        'phone'
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register(InquiryModal, InquiryModalAdmin)