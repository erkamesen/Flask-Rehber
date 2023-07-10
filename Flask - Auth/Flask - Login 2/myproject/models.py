from myproject import db, login_manager
from flask_bcrypt import Bcrypt
from flask_login import UserMixin

bcrypt = Bcrypt()


# Giriş yapan kullanıcının bilgilerini sessiona yüklemek için
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(128))

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
