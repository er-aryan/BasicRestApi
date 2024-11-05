
### Task 1: Setting up the Flask Application
import pymysql
pymysql.install_as_MySQLdb()

from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:0000@localhost/project'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_fallback_key')
app.config['JWT_SECRET_KEY'] = os.getenv('your_jwt_secret_key', 'default_fallback_key')
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)
jwt = JWTManager(app)


### Task 2: Error Handling
@app.errorhandler(400)
def bad_request_error(e):
    return jsonify(error='Bad Request'), 400

@app.errorhandler(401)
def unauthorized_error(e):
    return jsonify(error='Unauthorized'), 401

@app.errorhandler(404)
def not_found_error(e):
    return jsonify(error='Not Found'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify(error='Internal Server Error'), 500

### Task 3: Authentication
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

@app.route('/', methods=['GET'])
def index():
    return jsonify(message="Welcome to the Homepage!")

@app.route('/register', methods=['POST'])
@jwt_required() 
def create_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify(message="Username and password are required"), 400

    # Check if the user already exists
    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify(message="User already exists"), 409  

    # Create new user
    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify(message="User created successfully"), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(message='Invalid credentials'), 401

@app.route('/admin', methods=['GET'])
@jwt_required()
def admin():
    return jsonify(message='Welcome to the admin route!'), 200

### Task 4: File Handling
@app.route('/upload', methods=['POST'])
@jwt_required()
def upload_file():
    if 'file' not in request.files:
        return jsonify(message='No file part'), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify(message='No selected file'), 400
    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return jsonify(message='File uploaded successfully'), 201

### Task 5: Public Route
@app.route('/public', methods=['GET'])
def public():
    return jsonify(message='This is public information available without authentication'), 200

### Task 6: Services
@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify(users=[{'id': user.id, 'username': user.username} for user in users]), 200

@app.route('/user/<int:id>', methods=['PUT'])
@jwt_required()
def update_user(id):
    data = request.get_json()
    user = User.query.get_or_404(id)
    user.username = data['username']
    user.password = data['password']
    db.session.commit()
    return jsonify(message='User updated successfully'), 200

@app.route('/user/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_user(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(message='User deleted successfully'), 200

if __name__ == '__main__': 
    app.run(debug=True)

