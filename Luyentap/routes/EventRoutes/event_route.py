from flask import Blueprint
from controllers.EventControllers import event_controller

event_bp = Blueprint('event_bp', __name__)

# Lấy toàn bộ sự kiện
@event_bp.route('/api/events', methods=['GET'])
def get_all_events():
    return event_controller.get_all_events()