from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class Client(models.Model):
    """Client model for food bank intake and eligibility tracking"""
    
    # Basic Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    
    # Address Information
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, default='CA')
    zip_code = models.CharField(max_length=10)
    
    # Household Information
    household_size = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Number of people in household"
    )
    monthly_income = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Total monthly household income"
    )
    
    # Eligibility Information
    ELIGIBILITY_CHOICES = [
        ('eligible', 'Eligible'),
        ('not_eligible', 'Not Eligible'),
        ('pending', 'Pending Review'),
    ]
    eligibility_status = models.CharField(
        max_length=20,
        choices=ELIGIBILITY_CHOICES,
        default='pending'
    )
    eligibility_notes = models.TextField(blank=True, help_text="Notes about eligibility determination")
    
    # Intake Information
    intake_date = models.DateTimeField(default=timezone.now)
    intake_staff = models.CharField(max_length=100, blank=True, help_text="Staff member who conducted intake")
    special_notes = models.TextField(blank=True, help_text="Any special dietary needs or notes")
    
    # Tracking
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_visit_date = models.DateField(null=True, blank=True)
    visit_count = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['-intake_date']
        verbose_name = "Client"
        verbose_name_plural = "Clients"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.city}"
    
    def calculate_eligibility(self):
        """Calculate eligibility based on income guidelines (185% of federal poverty level)"""
        # Federal Poverty Guidelines 2024 (approximate)
        poverty_guidelines = {
            1: 15000,   # Annual income for 1 person
            2: 20000,   # Annual income for 2 people
            3: 25000,   # Annual income for 3 people
            4: 30000,   # Annual income for 4 people
        }
        
        # Get guideline for household size (use 4+ for larger households)
        guideline = poverty_guidelines.get(self.household_size, poverty_guidelines[4])
        # Add $5,000 for each additional person beyond 4
        if self.household_size > 4:
            guideline += (self.household_size - 4) * 5000
        
        # Calculate monthly threshold (185% of annual / 12)
        monthly_threshold = (guideline * 1.85) / 12
        
        return self.monthly_income <= monthly_threshold
    
    def save(self, *args, **kwargs):
        """Auto-calculate eligibility if not manually set"""
        if self.eligibility_status == 'pending':
            is_eligible = self.calculate_eligibility()
            self.eligibility_status = 'eligible' if is_eligible else 'not_eligible'
        super().save(*args, **kwargs)


class IntakeRecord(models.Model):
    """Track individual intake visits for clients"""
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='intake_records')
    visit_date = models.DateField(default=timezone.now)
    staff_member = models.CharField(max_length=100, blank=True)
    notes = models.TextField(blank=True)
    items_received = models.TextField(blank=True, help_text="Items or services provided")
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-visit_date']
        verbose_name = "Intake Record"
        verbose_name_plural = "Intake Records"
    
    def __str__(self):
        return f"{self.client.first_name} {self.client.last_name} - {self.visit_date}"
