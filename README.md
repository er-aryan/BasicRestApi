# Flask RESTful API with JWT Authentication and File Handling

## Project Overview
This project is a RESTful API built using Flask that provides JWT authentication, error handling, file upload capabilities, and CRUD operations for user management using MySQL. 

## Features
- **JWT Authentication**: Secure access to protected routes with JSON Web Tokens.
- **Error Handling**: Custom error messages for common HTTP errors (400, 401, 404, 500).
- **File Handling**: Supports file uploads with validation.
- **CRUD Operations**: Full CRUD operations for managing users.
- **Public and Admin Routes**: Differentiated access levels for public and protected routes.

## Team Members
1. **Member 1**: Aryan Sharma
2. **Member 2**: Aviya Singh
3. **Member 3**: Cyrena Burke

## Prerequisites
- Python 3.10
- MySQL Server

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. **Set Up a Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Required Packages** (Install the required packages using requirements.txt)
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up MySQL Database**
    * Open MySQL and create a database for the project.
    * Update app.config['SQLALCHEMY_DATABASE_URI'] in app.py to use your database credentials:
      ```bash
      app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/database_name'
      ```
5. **Set Environment Variables** (Optional) <br> 
For production, set a strong SECRET_KEY and JWT_SECRET_KEY in your environment:
 ```bash
 export SECRET_KEY="your_secret_key"
 export JWT_SECRET_KEY="your_jwt_secret_key"
 ```
6. **Initialize the Database** <br> 
Ensure the database tables are created by running the following:
```bash
python
>>> from app import db
>>> db.create_all()
>>> exit()
```
##  Running the Application
1. Start the Flask application:
   ```bash
   flask run
    ```
2. Access the API: The API will be available at http://127.0.0.1:5000.

## API Endpoints
1. Authentication
  * POST /login: Log in and receive a JWT token.
2. User Management (JWT Protected)
  * POST /register: Create a new user.
  * GET /users: Get all users.
  * PUT /user/<id>: Update user information.
  * DELETE /user/<id>: Delete a user.
3. Public Routes
  * GET /public: Access publicly available information.
4. File Handling
  * POST /upload: Upload files (JWT Protected).
## Testing
  * Use Postman or similar tools to test each endpoint. Ensure to include the JWT token in the Authorization header for protected routes.


