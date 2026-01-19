# Generated manually

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('phone', models.CharField(blank=True, max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('street_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(default='CA', max_length=2)),
                ('zip_code', models.CharField(max_length=10)),
                ('household_size', models.PositiveIntegerField(help_text='Number of people in household', validators=[django.core.validators.MinValueValidator(1)])),
                ('monthly_income', models.DecimalField(decimal_places=2, help_text='Total monthly household income', max_digits=10)),
                ('eligibility_status', models.CharField(choices=[('eligible', 'Eligible'), ('not_eligible', 'Not Eligible'), ('pending', 'Pending Review')], default='pending', max_length=20)),
                ('eligibility_notes', models.TextField(blank=True, help_text='Notes about eligibility determination')),
                ('intake_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('intake_staff', models.CharField(blank=True, help_text='Staff member who conducted intake', max_length=100)),
                ('special_notes', models.TextField(blank=True, help_text='Any special dietary needs or notes')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('last_visit_date', models.DateField(blank=True, null=True)),
                ('visit_count', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'ordering': ['-intake_date'],
            },
        ),
        migrations.CreateModel(
            name='IntakeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visit_date', models.DateField(default=django.utils.timezone.now)),
                ('staff_member', models.CharField(blank=True, max_length=100)),
                ('notes', models.TextField(blank=True)),
                ('items_received', models.TextField(blank=True, help_text='Items or services provided')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intake_records', to='foodbank.client')),
            ],
            options={
                'verbose_name': 'Intake Record',
                'verbose_name_plural': 'Intake Records',
                'ordering': ['-visit_date'],
            },
        ),
    ]
