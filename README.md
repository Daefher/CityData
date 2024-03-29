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

1. **Start the Django development server:
   ```bash
    python manage.py runserver

Access the application at http://localhost:8000.

### API Usage

Endpoint: `/api/city-info`
This endpoint is designed to handle requests for city information, including dynamically generated summaries for each specified city. It accepts an array of city names and returns detailed information for each city, including a generated summary.

Request Format
To request information for one or more cities, send a POST request to `/api/city-info` with a JSON payload specifying the cities of interest in an array. For example, to request information for New York:

1. **
    ```bash
        POST /api/city-info
        Content-Type: application/json

        {
        "cities": ["New York"]
        }

2. ** Response Format
    The response is a JSON object containing a success message and an array of city information. Each city's information includes the name, population, geographical coordinates (latitude and longitude), region, and a dynamically generated summary.

    Example response for a request querying New York:
    ```bash
        {
            "success": "Cities updated successfully",
            "cities": [
                {
                    "name": "New York",
                    "population": 8419000,
                    "latitude": "40.66677",
                    "longitude": "-73.88236",
                    "region": "New York",
                    "summary": "New York, often called New York City, is the most populous city in the United States. It is known for its significant cultural, financial, and media impact globally. Key attractions include the Statue of Liberty, Central Park, and Times Square."
                }
            ]
        }

### Parameters

- **cities** (required): An array of city names for which information is requested.

### Success Response

-**success**: A message indicating the request was processed successfully.
-**cities**: An array containing detailed information for each requested city, including:
-**name**: The name of the city (String).
-**population**: The population of the city (Number).
-**latitude**: The latitude of the city (String).
-**longitude**: The longitude of the city (String).
-**region**: The region or state in which the city is located (String).
-**summary**: A dynamically generated summary providing an overview of the city (String).

### Error Responses

- If the request fails due to invalid input or server errors, an appropriate HTTP status code is returned along with a JSON object describing the error.

### Generating City Summaries

The application enhances the city information by adding AI-generated summaries for each city. These summaries are dynamically created at the time of the request using the Gemini API and are not stored in the database. This approach ensures that the summaries are up-to-date and can reflect recent changes or developments related to the city.

### Note on Data Storage

The AI-generated summaries are not stored in the application's database. They are generated in real-time upon each request, ensuring that the summaries provided are always generated from the most current data and insights available from the Gemini API. This design choice emphasizes the dynamic and up-to-date nature of the city summaries provided by the application.

### Note on Gemini AI API

It might need to Setup your API key again in the GEMINI APi documentation for this section to work. `https://ai.google.dev/tutorials/python_quickstart`