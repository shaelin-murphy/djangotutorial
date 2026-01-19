# Food Bank Management System - Starter Code

This is a Django starter project for a Food Bank Management System. It includes a complete Django application with client intake, eligibility tracking, and visit management features.

## Prerequisites

Before using this starter code, make sure you have Django installed. If you don't have Django installed, you can install it using:

```bash
pip install django
```

Or if you're using Python 3:

```bash
pip3 install django
```

## Setup Instructions

1. **Navigate to the project directory:**
   ```bash
   cd djangotutorial
   ```

2. **Run database migrations:**
   ```bash
   python manage.py migrate
   ```
   (Use `python3` instead of `python` if needed)

3. **Create a superuser (optional, for admin access):**
   ```bash
   python manage.py createsuperuser
   ```
   Follow the prompts to create an admin account.

4. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

5. **Access the application:**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Features

- **Client Management**: Register and track food bank clients
- **Eligibility Tracking**: Automatic eligibility calculation based on income guidelines
- **Visit Records**: Track individual client visits and items received
- **Search & Filter**: Search clients by name, city, or zip code, and filter by eligibility status
- **Dashboard**: View statistics about total clients, eligible clients, and pending reviews

## Project Structure

```
djangotutorial/
├── manage.py              # Django management script
├── mysite/                # Main project settings
│   ├── settings.py        # Project configuration
│   ├── urls.py           # Main URL routing
│   ├── wsgi.py           # WSGI configuration
│   └── asgi.py           # ASGI configuration
└── foodbank/             # Food bank application
    ├── models.py         # Database models (Client, IntakeRecord)
    ├── views.py          # View functions
    ├── urls.py           # App URL routing
    ├── forms.py          # Django forms
    ├── admin.py          # Admin interface configuration
    └── templates/        # HTML templates
        └── foodbank/
            ├── base.html
            ├── home.html
            ├── client_list.html
            ├── client_detail.html
            ├── client_intake.html
            └── add_intake_record.html
```

## Usage

After starting the server, you can:

1. **View the home page** - See dashboard statistics and recent clients
2. **Register a new client** - Click "New Intake" to add a new client
3. **View all clients** - Browse and search the client list
4. **View client details** - See full information about a specific client
5. **Add visit records** - Record visits and items provided to clients
6. **Use admin panel** - Access Django admin for advanced management

## Notes

- The database file (`db.sqlite3`) will be created automatically when you run migrations
- The eligibility calculation is based on 185% of federal poverty guidelines
- All templates use a modern, responsive design with a green color scheme

## Troubleshooting

If you encounter any issues:

1. Make sure Django is installed: `python -m django --version`
2. Ensure you're in the `djangotutorial` directory when running commands
3. Check that port 8000 is not already in use
4. Verify all migrations have been applied: `python manage.py showmigrations`
