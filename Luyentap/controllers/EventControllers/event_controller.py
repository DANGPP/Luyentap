from services.EventServices.event_service import EventService
from flask import jsonify, request
EV = EventService()



# lấy toàn bộ sự kiện
def get_all_events():
    return jsonify([u.to_dict() for u in EV.get_all_events()])
# thêm sự kiện mới
def add_new_event():
    data = request.get_json()
    
