from repositories.UserRepositories.user_repository import UserRepository as ur

class UserService:
    def __init__(self):
        self.repo = ur()

    def fetch_users(self):
        users = self.repo.get_all_users()
        return [u.to_dict() for u in users]
    
    # Lấy thông tin người dùng theo id
    def fetch_user_by_id(self, user_id):
        user = self.repo.get_user_by_id(user_id=user_id)
        if user:
            return user.to_dict()
        return None
    # cập nhật thông tin người dùng:
    def update_user(self, user_id, user_data_update):
        update_user = self.repo.update_user(user_id=user_id, user_data_update=user_data_update)
        if update_user == "UpdateDone":
            return "UpdateDone"
        return None
    