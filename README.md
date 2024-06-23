# Automated Sales System with Email Notifications

This project implements an automated sales system using Python, Flask, MySQL, and SMTP to manage customer orders and send purchase confirmation emails.

## Features

- **API Endpoint**: Provides endpoints to fetch existing orders (`GET /orders`) and add new orders (`POST /orders`).
- **Database Integration**: Utilizes MySQL database to store order details including customer information, order date, quantity, amount, payment mode, and status.
- **Email Notifications**: Automatically sends purchase confirmation emails to customers using SMTP upon successful order submission.
- **Data Validation**: Ensures required fields are provided during order submission and handles errors gracefully.
- **Error Handling**: Catches and logs errors encountered during database operations and email sending.

## Technologies Used

- **Python**: Programming language used for backend development.
- **Flask**: Micro web framework used to build the API endpoints.
- **MySQL**: Relational database management system used to store order data.
- **SMTP**: Protocol used for sending emails.
- **Requests**: Python library used to make HTTP requests to fetch data from the API.
- **datetime**: Python module used to handle date and time formatting.

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gautamraj8044/Automated-Sales-System-with-Email-Notifications.git
   cd Automated-Sales-System-with-Email-Notifications

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
4. **Database Setup:**
  Install MySQL and create a database named order.
  Modify database.py to set up the database connection with your MySQL credentials.
3. **Run the Flask application:**
   ```bash
   python app.py

