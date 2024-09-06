# Invoice Manager App

The **Invoice Manager App** is a Django-based application that helps manage invoices, products, and customer data. It includes features for uploading product data, generating PDF invoices, viewing and deleting invoices and products, and exporting data to Excel.

## Features

- **Product Management:**
  - Create, view, edit, and delete products.
  - Upload product data from Excel.
- **Invoice Management:**
  - Create and view invoices with customer details.
  - View detailed invoice information.
  - Delete invoices.
- **Export Data:**
  - Download invoices and product details to an Excel file.
- **PDF Invoice Generation:**
  - Generate a detailed PDF of an invoice for customers.

## Tech Stack

- **Frontend:** HTML, CSS
- **Backend:** Django (Python)
- **Database:** SQLite (default with Django)
- **Libraries:** 
  - Pandas (for Excel file handling)
  - Django forms and models

## Setup and Installation

### Prerequisites

- Python 3.x
- Django 3.x or newer
- Pandas

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/invoice-manager-app.git
   cd invoice-manager-app

2. **Install Required Dependencies: Install the required dependencies using pip:**

    ```bash
    pip install -r requirements.txt
3. **Apply Migrations: Run the following command to apply migrations and set up the database:**

    ```bash
    python manage.py migrate
4. **Create Superuser: To access the Django admin, create a superuser:**

    ```bash
    python manage.py createsuperuser
5. **Run the Development Server: Start the server to access the app:**

    ```bash
    python manage.py runserver
Access the App: Open your browser and go to http://127.0.0.1:8000/.

### Usage
**Dashboard:**

View the total number of products, invoices, and total income.
**Product Management:**

Add, edit, and delete products.
**Invoice Management:**

Create invoices for customers, including selecting products and quantities.
Automatically calculate the total invoice amount.
View invoice details or delete invoices.