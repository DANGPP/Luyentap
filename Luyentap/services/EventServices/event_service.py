from repositories.EventRepositories import event_repo


class EventService:
    def __init__(self):
        self.event_repo = event_repo.EventRepository()
    
    # Lấy toàn bộ sự kiện
    def get_all_events(self):
        return self.event_repo.get_all_events()
    # thêm sự kiện mới
    def add_new_event(self, event_data):
        return self.event_repo.add_new_event(event_data)
    