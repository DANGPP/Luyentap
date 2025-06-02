from repositories.AuthRepositories.auth_repo import AuthRepo
import jwt
import datetime
# from werkzeug.security import check_password_hash
def check_pass(passA, passB):
    if passA != passB:
        return None
    return True 
class AuthService:
    def __init__(self):
        self.AuthRepo = AuthRepo()
    # Tạo token 
    def generrate_token(self, user):
        payload = {
            'user_id': user.id,
            'email': user.email,
            'role': user.role,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, 'No_KEY', algorithm = 'HS256')
        return token
    # Xác thực đăng nhập
    def authenticate(self, email_typed,password_typed):
        user= self.AuthRepo.find_by_email(email_typed)
        if not user:
            return None
        if not check_pass(user.password, password_typed):
            return None
       
        return user
    # tạo người dùng mới
    def create_new_user_sv(self, new_user):
        user = self.AuthRepo.find_by_email(new_user.get('email'))
        if user:
            return "exited_register"
        return self.AuthRepo.create_new_user(new_user=new_user)