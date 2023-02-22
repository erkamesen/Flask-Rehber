# Flask - Login

Bu projede içinde userlarımızı barındıran bir database oluşturucaz. Kayıt olan kişiler */secrets* endpointimizde ki linkle beraber belirlediğimiz dosyayı indirebilecekler.


Libraries:

```py
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash

from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
```

```py
app = Flask(__name__)
login_manager = LoginManager()

app.config['SECRET_KEY'] = 'secret-key-goes-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'


db = SQLAlchemy(app)


@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
```

>LoginManager() sınıfından login_manager adında bir obje yaratıp bunu uygulamamızla eşliyoruz.


 ```py
@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))
```

Bu decorator ile birlikte giriş yapılan kullanıcıları yönetimimize alıyoruz.


```py
##CREATE TABLE

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(100), unique=True)
	password = db.Column(db.String(100))
	name = db.Column(db.String(1000))

with app.appcontext()
  db.create_all()
```

Tablomuzu oluşturuyoruz fakat kullanıcı işlemleri için classımıza sadece *db.Model* değil *UserMixin* classından da miras alıyoruz.

ID miz primary key onu otomatik olarak sistem atıyor zaten. Email ise unique olan kısım eğer sistemde aynı email de başka kullanıcı varsa /register endpointinde *flash()* ile uyarı oluşturuyoruz.

Son olarak with ile tabloyu oluşturup bu bölümü siliyoruz ki her uygulamayı çalıştırdığımızda tablo oluşturmasın. Zaten eğer bu bölüm kalırsa çalıştığı zaman *IntegrityError* yada *StateError* alabiliyoruz.

```py
@app.route('/')
def home():	
	return render_template("index.html", logged_in=current_user.is_authenticated)
```

Anasayfamızda *login* yada *register* bölümleri giriş yapmış kullanıcıya görünmesin diye *logged_in = current_user.is_authenticated* adında bir değişken oluşturuyoruz. Eğer kullanıcı giriş yaparsa (current_user) *is_authenticated* değeri *True* olarak dönüyor ve base.html mizde şablonumuzda *if* ile yakalayarak ona göre gösterim yapıyoruz.

```html
		<ul class="navbar-nav ml-auto">
			<li class="nav-item">
				<a class="nav-link" href="{{ url_for('home') }}">Home</a>
			</li>
			{% if not logged_in: %}
			<li class="nav-item">
				<a class="nav-link" href="{{ url_for('login') }}">Login</a>
			</li>
			<li class="nav-item">
				<a class="nav-link" href="{{ url_for('register') }}">Register</a>
			</li>
			{% else %}

			<li class="nav-item">
				<a class="nav-link" href="{{ url_for('logout') }}">Log Out</a>
			</li>
			{% endif %}
		</ul>
```

>Eğer kullanıcı giriş yaparsa loggen_in True dönüyor dolayısıyla koşulumuz not sayesinde False dönceği için Login ve Register görünmeyecek fakat else durumu çalıştığı için Logout kısmı görünecek.


```py
@app.route('/register', methods=["GET", "POST"])
def register():
	if request.method == "POST":
		if User.query.filter_by(email=request.form.get('email')).first():
		#User already exists
			flash("You've already signed up with that email, log in instead!")
			return redirect(url_for('login'))
 
		hashed_password = generate_password_hash(form_password, method='pbkdf2:sha256',salt_length=8) # girilen şifreyi hashliyoruz
		new_user = User(email=form_email, password=hashed_password, name=form_name) 
		# veritabanına ekliyoruz.
		db.session.add(new_user)
		db.session.commit()

		#Kullanıcıyı giriş yapmak için login sayfasına yönlendiriyoruz.
		return redirect(url_for('login'))  
    else:
        return render_template("register.html", logged_in=current_user.is_authenticated)
```

*POST* methodlarını yakalıyoruz. 
Eğer veritabanımızda formumuzdan gelen mail var ise *flash()* ile kullanıcıya bu mail zaten kayıtlı diye uyarı veriyoruz ve login sayfasına yönlendiriyoruz.

Eğer veritabanında kullanıcının girdiği mail yok ise o zaman maili ve ismi veritabanına hiç oynamadan kaydediyoruz.

*generate_password_hash(
		request.form.get('password'),
		method='pbkdf2:sha256',
		salt_length=8
		)*

ile beraber form dan aldığımız şifreyi 8 kere saltlayıp hashleyip veritabanımıza öyle kaydediyoruz. *check_password_hash* ile bu şifreyi login kısmında kontrol edebiliriz.

*new_user* ımızı ( tablo objesi ) veritabanımıza kaydediyoruz. Ardından *login_user(new_user)* ile oturumu açıp /secrets endpointine yolluyoruz.


```py
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
```


Login kısmımızda formdan gelen mail ile veritabanınından kullanıcımızı çekiyoruz.

Eğer gelen kullanıcı yok ise flash() ile maili kontrol edin mesajı yolluyoruz.

check_password_hash(user.password, password):

ile ilk parametreyi kullanıcının şifresini 2. parametreye ise form dan gelen parolayı yazıp karşılaştırıyoruz. Eğer şifreler birbiri ile eşleşmiyorsa flash() ile Lütfen şifrenizi kontrol ediniz mesajı yolluyoruz.

Eğer şifre de doğru ise login_user(user) ile kullanıcımızı aktif ediyoruz ve redirect(url_for('secrets')) sayfasına yolluyoruz.

Eğer *GET* isteği geldiyse ;

return render_template("login.html", logged_in=current_user.is_authenticated)

ile kullanıcı giriş yapmış mı diye kontrol yolluyoruz.



```py
@app.route('/secrets')
@login_required
def secrets():
	return render_template("secrets.html", name=current_user.name, logged_in=True)
```


>login_required decoratoru ile girişimizi ayarlıyoruz.


secrets.html  üstündeki "Welcome {{ user }}" kısmına parametre olarak current_user.name ile giriş yapan kullanıcının ismini yolluyoruz.


```py
@app.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('home'))
```


Eğer logout linkine basılırsa bu fonksiyon tetikleniyor ve *logout_user*() kullanıcı çıkışını yapıyor .
Ardından home sayfasına yönlendiriliyor.


```py
@app.route('/download')
@login_required
def download():
	return send_from_directory('static', filename="files/cheat_sheet.pdf")
```

>send_from_directory(rootfile, filename)

ile dosyamızı download ettirdik. Kök dizinimizi belirttikten sonra gerisini path olarak veriyoruz.


