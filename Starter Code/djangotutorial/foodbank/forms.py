from django import forms
from .models import Client, IntakeRecord


class ClientIntakeForm(forms.ModelForm):
    """Form for new client intake"""
    
    class Meta:
        model = Client
        fields = [
            'first_name', 'last_name', 'date_of_birth',
            'phone', 'email',
            'street_address', 'city', 'state', 'zip_code',
            'household_size', 'monthly_income',
            'eligibility_notes', 'special_notes', 'intake_staff'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'phone': forms.TextInput(attrs={'placeholder': '(555) 123-4567'}),
            'email': forms.EmailInput(attrs={'placeholder': 'email@example.com'}),
            'monthly_income': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
            'household_size': forms.NumberInput(attrs={'min': '1'}),
            'eligibility_notes': forms.Textarea(attrs={'rows': 3}),
            'special_notes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth',
            'household_size': 'Household Size',
            'monthly_income': 'Monthly Income ($)',
            'eligibility_notes': 'Eligibility Notes',
            'special_notes': 'Special Notes (Dietary needs, etc.)',
            'intake_staff': 'Intake Staff Member',
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make required fields more obvious
        for field_name, field in self.fields.items():
            if field.required:
                field.widget.attrs['required'] = True


class IntakeRecordForm(forms.ModelForm):
    """Form for recording a client visit"""
    
    class Meta:
        model = IntakeRecord
        fields = ['visit_date', 'staff_member', 'notes', 'items_received']
        widgets = {
            'visit_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
            'items_received': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'visit_date': 'Visit Date',
            'staff_member': 'Staff Member',
            'notes': 'Visit Notes',
            'items_received': 'Items/Services Provided',
        }
