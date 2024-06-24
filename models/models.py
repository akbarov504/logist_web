from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
from flask_login import LoginManager, UserMixin

db = SQLAlchemy()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id, is_deleted=False).first()

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(length=100), nullable=False)
    last_name = db.Column(db.String(length=100), nullable=False)
    phone = db.Column(db.String(length=50), unique=True, nullable=False)
    password = db.Column(db.String(length=300), nullable=False)
    chat_id = db.Column(db.BigInteger(), nullable=False)
    lang = db.Column(db.String(length=10), nullable=False)
    role = db.Column(db.String(length=300), nullable=False)
    publish_day = db.Column(db.Integer(), default=0)
    is_active = db.Column(db.Boolean(), default=True)

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    
    def __init__(self, first_name: str, last_name: str, phone: str, password: str, chat_id: int, lang: str, role: str, publish_day: int, is_active: bool, created_by: int) -> None:
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.password = password
        self.chat_id = chat_id
        self.lang = lang
        self.role = role
        self.publish_day = publish_day
        self.is_active = is_active
        self.created_by = created_by

    def get_id(self):
        return str(self.id)

class PromoCode(db.Model):
    __tablename__ = "promo_code"

    id = db.Column (db.Integer(), primary_key=True)
    name = db.Column(db.String(length=100), nullable=False)
    publish_day = db.Column(db.Integer(), nullable=False)
    expire = db.Column(db.DateTime(timezone=True))
    is_active = db.Column(db.Boolean(), default=True)

    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __init__(self, name: str, publish_day: int, is_active: bool, created_by: int) -> None:
        super().__init__()
        self.name = name
        self.publish_day = publish_day
        self.is_active = is_active
        self.expire = datetime.now() + timedelta(minutes = 5)
        self.created_by = created_by

class Offer(db.Model):
    _tablename_ = "offer"
    
    id = db.Column (db.Integer(), primary_key=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    month = db. Column(db.Integer(), nullable=False)
    is_active = db.Column(db.Boolean(), default=True)
    
    is_deleted = db.Column(db.Boolean(), default=False)
    created_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    created_by = db.Column(db.Integer(), db.ForeignKey("user.id"))
    updated_at = db.Column(db.DateTime(timezone=True), default=datetime.now())
    updated_by = db.Column(db.Integer(), db.ForeignKey("user.id"))

    def __init__(self, price: int, month: int, is_active: bool, created_by: int) -> None:
        super().__init__()
        self.price = price
        self.month = month
        self.is_active = is_active
        self.created_by = created_by
