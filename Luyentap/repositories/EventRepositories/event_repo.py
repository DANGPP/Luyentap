from models.model import Event, db
from datetime import date

class EventRepository:
    def __init__(self):
        self.Event = Event
    # lấy toàn bộ sự kiện
    def get_all_events(self):
        return self.Event.query.all();
    
    # Lấy sự kiện theo ID
    
    # thêm sự kiện mới
    def add_new_event(self, event_data):
        try:
            new_event = self.Event(
                eventname = event_data.get('eventname'),
                ngaytao = date.today(),
                totalbill = event_data.get('totalbill'),
                sotiendadong = 0,
            )
            db.session.add(new_event)
            db.session.commit()
            return new_event
        except Exception as ex:
            db.session.rollback()
            print("Lỗi ở add_new_event trong event_repo.py")
            return None