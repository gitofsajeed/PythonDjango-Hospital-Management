from django import forms
from .models import Booking, ContactUs



class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date': DateInput()
        }

        labels ={
            'p_name': "Pataient Name",
            'p_phone': "Contact Number",
            'p_email': "Email",
            'doc_name':"Doctor to Consult",
            'booking_date': "Booking Date"
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'

        labels ={
                'name': "Enter your name",
                'email': "Enter your email",
                'p_number': "Enter your contact number",
                'subj':"Subject",
                'msg': "Your message:"
            }
        