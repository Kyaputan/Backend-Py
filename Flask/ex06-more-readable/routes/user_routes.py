from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from database.db import db
from models.user import User

user_bp = Blueprint('users', __name__)

@user_bp.route('/')
def index():
    """Home page route"""
    return render_template('index.html')

@user_bp.route('/users')
def users():
    """List all users"""
    users = User.query.all()
    return render_template('users.html', users=users)

@user_bp.route('/users/create', methods=['GET', 'POST'])
def create_user():
    """Create a new user"""
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        
        # Validate input
        if not username or not email:
            flash('Username and email are required', 'danger')
            return render_template('create_user.html')
        
        # Check if user already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists', 'danger')
            return render_template('create_user.html')
        
        # Create new user
        new_user = User(username=username, email=email)
        
        try:
            db.session.add(new_user)
            db.session.commit()
            flash('User created successfully', 'success')
            return redirect(url_for('users.users'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error creating user: {str(e)}', 'danger')
    
    return render_template('create_user.html')

@user_bp.route('/users/<int:user_id>')
def get_user(user_id):
    """Get a specific user"""
    user = User.query.get_or_404(user_id)
    return jsonify(user.serialize())

@user_bp.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
def edit_user(user_id):
    """Edit a user"""
    user = User.query.get_or_404(user_id)
    
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        
        # Validate input
        if not username or not email:
            flash('Username and email are required', 'danger')
            return render_template('edit_user.html', user=user)
        
        # Check if username exists and is not the current user
        existing_user = User.query.filter_by(username=username).first()
        if existing_user and existing_user.id != user.id:
            flash('Username already exists', 'danger')
            return render_template('edit_user.html', user=user)
        
        # Update user
        user.username = username
        user.email = email
        
        try:
            db.session.commit()
            flash('User updated successfully', 'success')
            return redirect(url_for('users.users'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error updating user: {str(e)}', 'danger')
    
    return render_template('edit_user.html', user=user)

@user_bp.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    """Delete a user"""
    user = User.query.get_or_404(user_id)
    
    try:
        db.session.delete(user)
        db.session.commit()
        flash('User deleted successfully', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting user: {str(e)}', 'danger')
    
    return redirect(url_for('users.users'))

# API endpoints for CRUD operations
@user_bp.route('/api/users', methods=['GET'])
def api_get_users():
    """API endpoint to get all users"""
    users = User.query.all()
    return jsonify([user.serialize() for user in users])

@user_bp.route('/api/users', methods=['POST'])
def api_create_user():
    """API endpoint to create a user"""
    data = request.json
    
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Username and email are required'}), 400
    
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({'error': 'Username already exists'}), 400
    
    new_user = User(username=data['username'], email=data['email'])
    
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.serialize()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@user_bp.route('/api/users/<int:user_id>', methods=['PUT'])
def api_update_user(user_id):
    """API endpoint to update a user"""
    user = User.query.get_or_404(user_id)
    data = request.json
    
    if not data:
        return jsonify({'error': 'No data provided'}), 400
    
    if 'username' in data:
        existing_user = User.query.filter_by(username=data['username']).first()
        if existing_user and existing_user.id != user.id:
            return jsonify({'error': 'Username already exists'}), 400
        user.username = data['username']
    
    if 'email' in data:
        user.email = data['email']
    
    try:
        db.session.commit()
        return jsonify(user.serialize())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@user_bp.route('/api/users/<int:user_id>', methods=['DELETE'])
def api_delete_user(user_id):
    """API endpoint to delete a user"""
    user = User.query.get_or_404(user_id)
    
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'User deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500