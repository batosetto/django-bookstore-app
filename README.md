# Django Bookstore Application

A full-featured bookstore application built with **Python** and **Django**, offering functionalities like book listing, CRUD operations, user authentication, role-based access, and API integration with **Django Rest Framework**. The project utilizes **MySQL** for database management.

## Features

- **Book Listing**: Displays a list of available books with detailed views for each book.
- **CRUD Operations**: Allows adding, editing, and deleting books.
- **User Authentication**: Supports user registration, login, and logout functionality.
- **Role-Based Access**: Implements access control where only certain users can perform specific actions (e.g., book editing).
- **API Integration**: Provides API endpoints using Django Rest Framework for easy data access.
- **MySQL Database**: Stores all the application data securely and efficiently.

## Technologies Used

- **Backend**: Python, Django, Django Rest Framework
- **Frontend**: HTML, CSS, JavaScript (Django templates)
- **Database**: MySQL
- **Version Control**: Git, GitHub

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/batosetto/django-bookstore-app.git
   cd django-bookstore-app

2. **Create a virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt

4. **Set up MySQL database**:
    - Create a MySQL database for the project.
    - Update the database credentials in the settings.py file.

5. **Apply the  migrations**:
    ```bash
    python manage.py migrate

6. **Run the application**:
    ```bash
    python manage.py runserver

    

## Usage

- The application will be available at http://127.0.0.1:8000/.
- Register as a new user or log in with an existing account.
- Add, view, update, or delete books as per your role's permissions.
- Access API endpoints via /api/books/.

## Contributing

- Fork the repository.
- Create a new branch (git checkout -b feature-branch).
- Make your changes.
- Push to the branch (git push origin feature-branch).
- Create a pull request.

**License**
This project is licensed under the MIT License. See the LICENSE file for details.
