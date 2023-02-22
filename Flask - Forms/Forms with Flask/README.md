# Formlar

Kısaca özetlemek gerekirse import ettiğimiz FlaskForm classından inheritance alan yeni bir class oluşturup, wtforms paketindeki
Fieldları(HTML de ki input 'type' lar diyebiliriz.) bu child class içinde oluşturuyoruz. Bu classdan oluşturduğumuz objeyi
göndermek istediğimiz HTML sayfasını render_template ile renderlarken parametre olarak yolluyoruz ve HTML sayfasında bu formu basit bir 
şekilde oluşturuyoruz. <br>

Burada formdan aldığımız bilgilerini txt dosyasına yazarak kendi küçük veritabanımızı oluşturucaz.

Paket kurulumu:
```
pip install flask_wtf
```

- flask_wtf paketinden FlaskForm classını import ediyoruz.
- wtforms paketinden formumuzda kullanacağımız field ları import ediyoruz.

```
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, SubmitField
```

Form üzerinden oluşabilecek olan CRF lere karşı korunmak için uygulamamıza bir secret_key belirliyoruz.

```
app.config["SECRET_KEY"] = "herhangibirsey"
```

Form oluşturmak için bir class oluşturup FlaskForm sınıfından inheritance alıyoruz.Ardından wtform modülünden import ettiğimiz fieldlar ile oluşturduğumuz class niteliklerinin her biri bizim formumuzun bir alanı oluyor.

```
class ContactForm(FlaskForm):
    name = StringField("İsim")
    email = EmailField("Email")
    msg = StringField("Mesaj")
    submit = SubmitField("Yolla")
```
Burda oluşturduğumuz class ile aslında bir iletişim formu oluşturduk. kullanıcıdan isim, email ve mesaj alarak submit ile serverimiza işlenmek üzere bilgileri yollayabiliyoruz. <br>

Şimdi artık route umuzu oluşturup gelen istekleri dinleyebiliriz. Bir route oluşturup form classından oluşturduğumuz nesneyi gelen GET isteği ile beraber HTML sayfasına gömülü şekilde kullanıcıya yolluyoruz.

```
@app.route("/", methods=["GET","POST"])
def index():
    form = ContactForm()
    if request.method == "POST":
        isim = request.form.get("name", "bilinmiyor")
        email = request.form.get("email", "email girilmedi")
        mesaj = request.form.get("msg", "mesaj girilmedi")
        with open("veritabani.txt", "a") as f:
            f.write(f"isim: {isim}, email: {email}, mesaj: {mesaj}")
            print("deneme")
        return redirect(url_for("index"))
    return render_template("index.html", form=form)
```

teker teker incelemek gerekirse:
```
@app.route("/", methods=["GET","POST"])
```
"/" endpointinde gelen istekleri dinliyoruz. Gelen GET ve POST requestlere cevap döndüreceğimizi de methods parametresi ile belirtiyoruz.
```
def index():
```
URL mize istek geldiği zaman tetiklenecek fonksiyonumuzu belirtiyoruz.
```
form = ContactForm()
...
...
...
...
return render_template("index.html", form=form)
```
eğer gelen istek GET ise classımızdan oluşturduğumuz form objesini işlenmek üzere HTML sayfasına render_tempalte() fonksiyonuna parametre olarak yolluyoruz.

```
if request.method == "POST":
        isim = request.form.get("name", "bilinmiyor")
        email = request.form.get("email", "email girilmedi")
        mesaj = request.form.get("msg", "mesaj girilmedi")
```
Eğer gelen istek POST ise çalışacak olan kısmımız burası. Formdan girilmiş olan isim, email ve mesaj bilgisini request.form.get() ile tam olarak sözlük mantığında işlenmek üzere server tarafımıza çekiyoruz. Burada 2. parametre tam olarak sözlük mantığında eğer bilgiyi çekemezsek döndüreceğimiz default değerdir.

```
with open("veritabani.txt", "a") as f:
            f.write(f"isim: {isim}, email: {email}, mesaj: {mesaj}")
```
formdan aldığımız bilgileri yazmak için veritabanı niyetine txt dosyasında bilgilerimi saklıyoruz.

```
return redirect(url_for("index"))
```
en son index fonksiyonunu tekrar tetikleyerek formumuzun olduğu sayfayı tekrar döndürüyoruz.

## HTML Kısmı

```
  <form action="{{ url_for('index')}}" method="post">
        {{ form.name.label }}
        {{ form.name(class="buraya-sinif-gelebilir") }} <br>
        {{ form.email.label }}
        {{ form.email(style="background-color:yellow;") }} <br>
        {{ form.msg.label }}
        {{ form.msg }} <br>
        {{ form.submit }}
    </form>
```

Yolladığımız form nesnesini jinja2 şablon motoru ile HTML dosyasında işlemek için {{ }} aralarına class niteliklerimizi yani fieldlarımızı yerleştiriyoruz. <br>
action kısmına bilgileri yollayacağımız fonksiyonu url_for ile yolluyoruz, method kısmına ise POST request atacağımızdan post olarak belirtiyoruz. <br>
Ayrıca name ve email fieldlarından görüldüğü üzere parantez içinde class ve style gibi bir çok şeyi yani HTML formu oluştururken yapabildiğimiz her şeyi yapabiliyoruz.
