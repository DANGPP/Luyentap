from models.model import User
from extension import db
class UserRepository:
    def __init__(self, User=User):
        self.User = User

    def get_all_users(self):
        return self.User.query.all()

    # Lấy thông tin người dùng theo ID
    def get_user_by_id(self, user_id):
        return self.User.query.filter_by(id = user_id).first()
    
    #Cập nhật thông tin người dùng, user_data_update laf dict 
    def update_user(self, user_id, user_data_update):
        try:
            user = self.get_user_by_id(user_id)
            user.hovaten = user_data_update.get('hovaten', user.hovaten)
            user.ngaysinh = user_data_update.get('ngaysinh', user.ngaysinh)
            user.sdt = user_data_update.get('sdt', user.sdt)
            user.tennganhang = user_data_update.get('tennganhang', user.tennganhang)
            user.stknh = user_data_update.get('stknh', user.stknh)
            user.email = user_data_update.get('email', user.email)
            user.password = user_data_update.get('password', user.password)
            db.session.commit()
            # return user.to_dict()
            return "UpdateDone"
        except Exception as ex:
            db.session.rollback()
            print(f"Error updating user: {ex}")
            return None
    