from django.contrib import admin
from .models import Departments, Doctors, Booking, ContactUs

# Register your models here.


admin.site.register(Departments)
admin.site.register(Doctors)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','email', 'p_number', 'subj', 'msg')
admin.site.register(ContactUs, ContactAdmin)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'p_name','p_phone', 'p_email', 'doc_name', 'booking_date','booked_on')
admin.site.register(Booking,BookingAdmin)