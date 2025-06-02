from flask import request, jsonify
from services.AuthServices.auth_service import AuthService
auth_service = AuthService()

def login_controller():
    data = request.get_json()
    email= data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"message":"Nhập sai tài khoản hoặc mật khẩu"}),400
    user = auth_service.authenticate(email_typed=email, password_typed=password)
    if not user:
        return jsonify({"message": "Đăng nhập thất bại"}),401
    
    token = auth_service.generrate_token(user)
    return jsonify({"message": "Đăng nhập thành công",
                    "type": str(type(user)),
                    "access_token": token,
                    "user": user.to_dict()}),200


# controller đang ký:
# tạo schema cho form đang ký đăng nhập( không yêu cầu toàn bộ thông tin của db)
def register_controller():
    data =  request.get_json()
    for attribute in ('hovaten','ngaysinh','sdt','tennganhang','stknh','email','password'):
        if not data.get(attribute):
            return jsonify(
                {
                    "message": "Nhập thiếu thông tin"+attribute
                }
            )
    NewUser  = auth_service.create_new_user_sv(data)
    if NewUser == "exited_register":
        return jsonify(
                {
                    "message": "Người dùng đã tồn tại"
                }
            ),409
    return jsonify(
                {
                    "message": "Đã đăng ký thành công",
                    "NewUser": NewUser
                }
            )
