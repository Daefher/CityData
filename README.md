# City Summaries Web Application

## Project Overview

This web application showcases web pages for each of 10 selected cities in the United States, providing summarized data about each city, including population, area, and top attractions. Summaries are dynamically generated using the Gemini API, leveraging publicly available databases for initial data.

### Technology Stack

- **Backend**: Django, Django Rest Framework (DRF)
- **AI Tool for Summaries**: Gemini API
- **Data Fetching**: Requests library
- **Frontend**: HTML, CSS, JavaScript

## Setup and Installation

### Requirements

- Python 3.8+
- pip and virtualenv

### Installation Steps

1. **Environment Setup**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Unix/macOS
   venv\Scripts\activate  # Windows

2. **Dependency Installation**:
   ```bash
    pip install django djangorestframework requests

3. **Database Migrations**:
   ```bash
    python manage.py makemigrations
    python manage.py migrate

### Configuration  

Securely store and access your Gemini API key using environment variables or Django's settings. Ensure you do not hardcode this sensitive key in your source code.

### Running the Project

Start the Django development server:
   ```bash
    python manage.py runserver    

Access the application at http://localhost:8000.

### Running the Project


