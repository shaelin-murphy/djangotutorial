from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Client, IntakeRecord
from .forms import ClientIntakeForm, IntakeRecordForm


def home(request):
    """Home page with dashboard statistics"""
    total_clients = Client.objects.count()
    eligible_clients = Client.objects.filter(eligibility_status='eligible').count()
    pending_clients = Client.objects.filter(eligibility_status='pending').count()
    recent_clients = Client.objects.all()[:5]
    
    context = {
        'total_clients': total_clients,
        'eligible_clients': eligible_clients,
        'pending_clients': pending_clients,
        'recent_clients': recent_clients,
    }
    return render(request, 'foodbank/home.html', context)


def client_list(request):
    """List all clients with search functionality"""
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')
    
    clients = Client.objects.all()
    
    if search_query:
        clients = clients.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(city__icontains=search_query) |
            Q(zip_code__icontains=search_query)
        )
    
    if status_filter:
        clients = clients.filter(eligibility_status=status_filter)
    
    context = {
        'clients': clients,
        'search_query': search_query,
        'status_filter': status_filter,
    }
    return render(request, 'foodbank/client_list.html', context)


def client_detail(request, client_id):
    """View detailed information about a client"""
    client = get_object_or_404(Client, id=client_id)
    intake_records = client.intake_records.all()[:10]  # Last 10 visits
    
    context = {
        'client': client,
        'intake_records': intake_records,
    }
    return render(request, 'foodbank/client_detail.html', context)


def client_intake(request):
    """New client intake form"""
    if request.method == 'POST':
        form = ClientIntakeForm(request.POST)
        if form.is_valid():
            client = form.save()
            messages.success(request, f'Client {client.first_name} {client.last_name} has been successfully registered.')
            return redirect('foodbank:client_detail', client_id=client.id)
    else:
        form = ClientIntakeForm()
    
    return render(request, 'foodbank/client_intake.html', {'form': form})


def add_intake_record(request, client_id):
    """Add a new intake record for an existing client"""
    client = get_object_or_404(Client, id=client_id)
    
    if request.method == 'POST':
        form = IntakeRecordForm(request.POST)
        if form.is_valid():
            intake_record = form.save(commit=False)
            intake_record.client = client
            intake_record.save()
            
            # Update client's last visit and visit count
            client.last_visit_date = intake_record.visit_date
            client.visit_count += 1
            client.save()
            
            messages.success(request, f'Intake record added for {client.first_name} {client.last_name}.')
            return redirect('foodbank:client_detail', client_id=client.id)
    else:
        form = IntakeRecordForm()
    
    return render(request, 'foodbank/add_intake_record.html', {
        'form': form,
        'client': client,
    })
