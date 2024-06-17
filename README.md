# Django CSV Upload and Analysis Web Application

This Django web application allows users to upload CSV files, perform data analysis using Pandas and NumPy, and display the results and visualizations on a web interface.

## Features

1. **File Upload**: Users can upload CSV files for analysis.
2. **Data Processing**: The application reads the uploaded CSV file and performs basic data analysis:
   - Displays the first few rows of the data.
   - Calculates summary statistics (mean, median, standard deviation) for numerical columns.
   - Identifies and handles missing values.
3. **Data Visualization**: Generates basic plots using Matplotlib or Seaborn (integrated with Pandas) such as histograms for numerical columns.
4. **User Interface**: A simple and user-friendly interface to display the data analysis results and visualizations.

## Requirements

- Python  3.11.1
- Django  	4.2.13
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/vedant0611/ve3-assignment/tree/main
    cd application
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```

4. **Install the Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

5. **Apply Migrations**:
    ```bash
    python manage.py migrate
    ```

6. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

7. **Open the Application in Your Browser**:
    Open your web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. **Upload CSV File**:
    - On the homepage, use the form to upload a CSV file.
    - Click the "Diagnose" button to submit the file.

2. **View Results**:
    - After submitting the file, the application will display:
      - The first few rows of the uploaded CSV.
      - Summary statistics for numerical columns.
      - A table showing the number of missing values in each column.
      - Histograms for numerical columns.

## Sample CSV File

A sample CSV file `Placement_Data_Full_Class (1).csv` is included in the repository for testing purposes.

## Project Structure

```
django-csv-upload-analysis/
├── application/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
├── base/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   ├── templates/
│   │   └── base/
│   │       └── csvupload.html
│   ├── static/
│       └── css/
│           └── style.css
├── media/
│   ├── upload/
│       └── (uploaded files will be stored here)
├── manage.py
├── requirements.txt
├── README.md
└── sample.csv
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

