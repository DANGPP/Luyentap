from extension import db
from datetime import date

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    hovaten = db.Column(db.String(100), nullable=False)
    ngaysinh = db.Column(db.Date)
    sdt = db.Column(db.String(20))
    role = db.Column(db.String(20), default='staff')
    tennganhang = db.Column(db.String(100))
    stknh = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    events = db.relationship("EventUser", back_populates="user")
    payed_events = db.relationship("Event", back_populates="payedperson", foreign_keys="Event.payedperson_id")

    def to_dict(self):
        return {
            "id": self.id,
            "hovaten": self.hovaten,
            "ngaysinh": self.ngaysinh.strftime("%Y-%m-%d") if self.ngaysinh else None,
            "sdt": self.sdt,
            "role": self.role,
            "tennganhang": self.tennganhang,
            "stknh": self.stknh,
            "email": self.email,
            "password": self.password
        }

class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    eventname = db.Column(db.String(100), nullable=False)
    ngaytao = db.Column(db.Date, default=date.today)
    totalbill = db.Column(db.Numeric(15, 2), default=0.00)
    sotiendadong = db.Column(db.Numeric(15, 2), default=0.00)

    # Thêm cột payedperson_id
    payedperson_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="SET NULL"))
    payedperson = db.relationship("User", back_populates="payed_events", foreign_keys=[payedperson_id])

    users = db.relationship("EventUser", back_populates="event")

    def to_dict(self):
        return {
            "id": self.id,
            "eventname": self.eventname,
            "ngaytao": self.ngaytao.strftime("%Y-%m-%d"),
            "totalbill": float(self.totalbill),
            "sotiendadong": float(self.sotiendadong),
            "payedperson_id": self.payedperson_id
        }

class EventUser(db.Model):
    __tablename__ = 'event_user'
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id', ondelete="CASCADE"))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"))

    event = db.relationship("Event", back_populates="users")
    user = db.relationship("User", back_populates="events")

    __table_args__ = (
        db.UniqueConstraint('event_id', 'user_id', name='unique_event_user'),
    )

    def to_dict(self):
        return {
            "id": self.id,
            "event_id": self.event_id,
            "user_id": self.user_id
        }
