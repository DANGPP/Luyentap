from models.model import User
from extension import db

class AuthRepo:
    def __init__(self, User = User):
        self.user = User
    def find_by_email(self,email):
        return self.user.query.filter_by(email=email).first()
    
    # đăng ký người dùng mới- mặc định role là staff
    def create_new_user(self, new_user ):
        try:
            NewUser = self.user(
                hovaten = new_user.get('hovaten'),
                ngaysinh = new_user.get('ngaysinh'),
                sdt = new_user.get('sdt'),
                role = 'staff',
                tennganhang = new_user.get('tennganhang'),
                stknh = new_user.get('stknh'),
                email = new_user.get('email'),
                password = new_user.get('password')
            )

            db.session.add(NewUser)
            db.session.commit()
            return NewUser.to_dict()
        except Exception as ex:
            db.session.rollback()
            print(ex + "lỗi ở create_new_user của auth_repo.py")

        