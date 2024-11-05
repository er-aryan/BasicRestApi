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
    ![Screenshot from 2024-11-04 20-04-16](https://github.com/user-attachments/assets/21555436-31b4-4e96-9079-4c9cbdd21584)

2. User Management (JWT Protected)
  * POST /register: Create a new user.
    ![Screenshot from 2024-11-04 20-10-04](https://github.com/user-attachments/assets/a1186b88-6b34-4135-a44e-62b7440e4224)
    ![Screenshot from 2024-11-04 20-10-31](https://github.com/user-attachments/assets/324ce11d-ad11-48a8-8d5b-818696bf8933)
  * GET /users: Get all users.
    ![Screenshot from 2024-11-04 20-11-22](https://github.com/user-attachments/assets/ea7c6f68-4e90-497b-a7bd-1cbf3f625601)
  * PUT /user/<id>: Update user information.
    ![Screenshot from 2024-11-04 20-24-48](https://github.com/user-attachments/assets/5654cd6b-dc4c-4356-9e61-580518068e9c)
    ![Screenshot from 2024-11-04 20-26-09](https://github.com/user-attachments/assets/5986fd3e-3349-4b3f-b479-37e027db36fd)
  * DELETE /user/<id>: Delete a user.
    ![Screenshot from 2024-11-04 20-26-42](https://github.com/user-attachments/assets/a84b3970-8ed2-4bde-9b2c-54aaea58f389)
    ![Screenshot from 2024-11-04 20-27-36](https://github.com/user-attachments/assets/8eca1f90-b344-453e-bbe3-ea90be462ca1)

3. Public Routes
  * GET /public: Access publicly available information.
    ![Screenshot from 2024-11-04 20-28-13](https://github.com/user-attachments/assets/0204e0b2-096b-4fe5-abd2-5eb55dd20441)
4. File Handling
  * POST /upload: Upload files (JWT Protected).
    ![Screenshot from 2024-11-04 20-41-39](https://github.com/user-attachments/assets/3dcebf77-99ad-472a-947d-96e1c25a1778)
    ![Screenshot from 2024-11-04 20-42-49](https://github.com/user-attachments/assets/d2e70725-8055-4e67-a6f7-eb1c0c0358aa)

## Testing
  * Use Postman or similar tools to test each endpoint. Ensure to include the JWT token in the Authorization header for protected routes.
## Video Demonstration

https://github.com/user-attachments/assets/e858a02f-b757-49cb-bf76-b8c36a73a842

