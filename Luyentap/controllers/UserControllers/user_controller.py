from flask import jsonify, request
from services.UserServices.user_service import UserService as us
user_service = us()


# Lấy toàn bộ người dùng
def get_users():
    return jsonify(user_service.fetch_users())

# Lấy thông tin người dùng theo ID
def get_user_by_id(user_id):
    user = user_service.fetch_user_by_id(user_id=user_id)
    if user:
        return jsonify({"user": user}), 200
    else:
        return jsonify({"message": "User not found"}), 404
# Cập nhật thông tin người dùng
def update_user(user_id, user_data_update):
    data = request.get_json()
    result = user_service.update_user(user_id, data)
    if result == "UpdateDone":
        return jsonify({"message": "User updated successfully"}), 200
    else:
        return jsonify({"message": "Error updating user"}), 500