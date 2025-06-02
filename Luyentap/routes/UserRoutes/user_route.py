from flask import Blueprint
from controllers.UserControllers import user_controller

user_bp = Blueprint('user_bp',__name__)
# Lấy thoàn bộ người dùng
@user_bp.route('/api/users')
def home():
    return user_controller.get_users()
# Lấy thông tin 1 người dùng theo ID
@user_bp.route('/api/users/<int:user_id>')
def get_user(user_id):
    return user_controller.get_user_by_id(user_id)
# Cập nhật thông tin ngời dùng
@user_bp.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    return user_controller.update_user(user_id, user_data_update=None)