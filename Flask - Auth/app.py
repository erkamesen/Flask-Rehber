from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, login_required, current_user, logout_user, LoginManager

app = Flask(__name__)
login_manager = LoginManager(app)
# Bu nesne, oturum açmak için kullanılan ayarları tutmak için kullanılır.

app.config['SECRET_KEY'] = 'thisisasecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

""" with app.app_context():
    db.drop_all()
    db.create_all() """

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    # form dan POST request atıldığında aşağıdaki if tetiklenecek.
    if request.method == 'POST':
        # formdan girilen bilgileri bir değişkene atıyoruz.
        form_email = request.form.get('email')
        form_name = request.form.get('name')
        form_password = request.form.get('password')
        hashed_password = generate_password_hash(form_password, method='pbkdf2:sha256',salt_length=8) # girilen şifreyi hashliyoruz
        new_user = User(email=form_email, password=hashed_password, name=form_name) 
        # veritabanına ekliyoruz.
        db.session.add(new_user)
        db.session.commit()
        
        #Kullanıcıyı giriş yapmak için login sayfasına yönlendiriyoruz.
        return redirect(url_for('login'))  
    else:
        return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        form_email = request.form.get('email')
        form_password = request.form.get('password')
        user = User.query.filter_by(email=form_email).first()
        if user:
            if check_password_hash(user.password, form_password):
                login_user(user)
                return redirect(url_for('secrets'))
            else:
                flash('Lütfen şifrenizi kontrol ediniz.')
                return render_template("login.html")
        else:
            flash('Lütfen maili kontrol ediniz.')
            return render_template("login.html")        
        
    else:
        return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
	return render_template("secrets.html", user=current_user.name, logged_in=True)


@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('home'))
    


@app.route('/download')
def download():
    return send_from_directory('static', path="files/wallpaper.jpeg")


if __name__ == "__main__":
    app.run(debug=True)
