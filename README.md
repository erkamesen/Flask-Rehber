# Flask-Rehber

<p>
  <img align="left" width="500" height="300" src="https://user-images.githubusercontent.com/120065120/212087425-6ee72546-16fc-476a-9067-54de6a4efbd9.png" />
Flask, hafif bir WSGI web uygulama frameworkudur. Karmaşık uygulamalara ölçeklenebilme özelliğiyle hızlı ve kolay bir başlangıç yapmak için tasarlanmıştır.<br>
Flask size sadece öneriler sunar herhangi bir bağımlılık veya proje düzenine zorlamaz. Kullanmak istedikleri toolları ve libraryleri seçmek geliştiriciye kalır. Topluluk tarafından sağlanan ve yeni işlevler eklemeyi kolaylaştıran birçok paketi vardır.
</p>

<br><br><br><br>



## İçerik:
- [Flask Nedir ?](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#flask-nedir-)
- [Flask neden Microframework olarak geçiyor ?](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#flask-neden-microframework-olarak-ge%C3%A7iyor-)
- [Neden Flask ?](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#neden-flask-)
- [Flask Dependencies(Bağımlılıklar)](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#flask-dependenciesba%C4%9F%C4%B1ml%C4%B1l%C4%B1klar)
- [WSGI Nedir ?](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#wsgi-nedir-)
- [Werkzeug Nedir ?](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#werkzeug-nedir-)
- [Flask Kurulumu](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#flask-kurulumu)
- [Klasör Yapısı](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#klas%C3%B6r-yap%C4%B1s%C4%B1)
- [Flask ile Veritabanı Bağlantısı](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#flask-ile-veritaban%C4%B1-ba%C4%9Flant%C4%B1s%C4%B1)
- [Flsk ve SQLite](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#flask-ve-sqlite)
- [Jinja2 Template Sayfaları](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#jinja2-template-sayfalar%C4%B1)
- [Default Host ve Port](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#default-host-ve-port)
- [Basit Flask Uygulaması](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#basit-flask-uygulamas%C4%B1)
- [Route Değişkenleri](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#route-dei%C5%9Fkenleri)
- [HTTP Metotları](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#http-metotlar%C4%B1)
- [Flask ve Unique URL'ler](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#flask-ve-unique-urller)
--- 

## Flask Nedir ?

En kısa hali ile [Flask](https://flask.palletsprojects.com/en/2.2.x/) 2011 yılında Pocoo python topluluğundan 'Armin Ronacher' tarafından nisan şakası olarak çıkarılan, python dili ile yazılmış açık kaynak bir web geliştirme micro framework'üdür.(Web Framework).
Flask çabuk öğrenilebilen, kolay ve ihtiyacımız olan ek paketleri sonradan projemize dahil edebildiğimiz için projenin hantallaşmasını önleyen, route yapısı basit ve benchmarklarına bakıldığında performansı gayet yüksek bir frameworktür.
Python kodlarını yazmak için Django gibi Jinja2 şablon motorunu ve Werkzeug aracı ile WSGI arayüzünü kullanır.

---
## Flask neden Microframework olarak geçiyor ? 
- Flaskın microframework olarak adlandırılma sebebi; Flask yalnızca request, route ve blueprint gibi temel özellikleri bize sağlar. Flaskı kurduğumuz zaman minimal uygulamalar yapabiliriz fakat uygulamalarımız geliştikçe harici olarak caching, ORM, formlar vb. diğer özellikler için Flask-Extensions kullanmamız gerekiyor. Bunları da pip aracılığı ile kuruyoruz ve projemize import edebiliyoruz.
---
## Neden Flask ?
- Dahili bir geliştirme sunucusuna sahiptir.
- Geniş üçüncü taraf uzantıları vardır.
- Bir web geliştiricisi tarafından hızla öğrenilebilir.
- WSGI uyumludur.
- Unicode'u destekler.

---
## Flask Dependencies(Bağımlılıklar)
Flask kurulurken bu dağıtımlar otomatik olarak kurulacaktır:
- [Werkzeug](https://palletsprojects.com/p/werkzeug/) uygulamalar ve sunucular arasındaki standart Python arabirimi olan WSGI'yi uygular.
- [Jinja](https://palletsprojects.com/p/jinja/), uygulamanızın sunduğu sayfaları işleyen bir şablon dilidir.
- [MarkupSafe](https://palletsprojects.com/p/markupsafe/), Jinja ile birlikte gelir. Injection saldırılarından kaçınmak için şablonları işlerken güvenilmeyen girdilerden kaçar.
- [ItsDangerous](https://palletsprojects.com/p/itsdangerous/), uygulmada bütünlüğünü ve önemli verileri imzalayarak onların güvenliğini sağlar. Flask da genel olarak session ve cookie güvenliği için kullanılır.
- [Click](https://palletsprojects.com/p/click/), komut satırı uygulamaları yazmak için bir framework dür.
---
## WSGI Nedir ?

WSGI (Web Server Gateway Interface-Web Sunucusu Ağ Geçidi Arayüzü) python ile bir web uygulaması geliştirmek için kullanılan arayüzdür. Server olarak da adlandırılabilir.Web Server'ların python kodumuzu anlaması için bize aracılık eder. Sonuç olarak eğer WSGI kullanmazsak server yazdığımız kodları çalıştıramayacaktır.

---

## Werkzeug Nedir ?
Werkzeug requestleri, response ları ve diğer yardımcı fonksiyonları uygulayan bir WSGI toolkit idir.Python'da WSGI uyumlu bir web uygulaması oluşturmak için kullanılabilen bir library koleksiyonudur. Bir web sunucusu doğrudan Python ile iletişim kuramadığı için Python web uygulamaları için bir WSGI sunucusu gereklidir.

---
## Flask Kurulumu

### Environment(venv)
virtualenv, sanal Python ortamı oluşturucusudur.Kullanıcının birden çok Python ortamını yan yana oluşturmasına yardımcı olur, böylece library lerin farklı sürümleri arasındaki uyumluluk sorunlarını önleyerek düzgün şekilde çalışmasını sağlar. </br>
Aşağıdaki komutlar venv'i kurar:
```
pip install virtualenv
```
Bu komutun bir yöneticiye ihtiyacı var eğer Linux-Mac Os kullnıyorsak **pip** den önce **sudo** kullanabiliriz. </br>
Eğer windows kullanıyorsak Administrator olarak giriş yapmamız yeterliir.
```
sudo apt-get install virtualenv
```
Artık projemizin bulunduğu klasöre gidip sanal ortamımızı aktif edebiliriz. Terminalimizi projemiz içinde açıp:
```
virtualenv venv
```
Artık sanal ortamımızı projemizin içine kurduk aktif edip içine istediğimiz paketi pip ile kurabiliriz.(yeni bir sanal ortam oluşturduğumuz için daha önce kurduğunuz gömülü olmayan paketleri yine kuracaksınız.)

Linux/Os
```
venv/bin/activate
```
Windows:
```
venv/scripts/activate
```
Artık sanal ortamımıza flask kurabiliriz. 
Windows:
```
pip install flask
```
Linux-Mac:
```
pip3 install flask
```
---

## Klasör Yapısı
Basit bir flask uygulaması için klasör yapısı şu şekildedir:
```
/project
        /templates/
                   index.html
                   sayfa2.html
                   sayfa3.html
        /static/
              main.css
        /app.py
```
Flask uygulamamızda Flask sınıfından objemizi initialize ettiğimiz .py dosyamızın içinde bulunduğu klasör içindeki: 
- /templates klasörü içine HTML dosyalarımızı oluşturuyoruz.
- /static klasörü içinde CSS , assets , resim dosyalarımızı  oluşturuyoruz.
Bu yapı objemizi oluşturduğumuz python dosyasına göre default şekilde ayarlıdır ve dileğe göre obje oluşturulurken parametre olarak path değiştirilebilir.(-zorda kalmdıkça tavsiye edilmez-) Özellikle Blueprint le çalışırken blueprintlerimizi views klasörü içinde oluşturulabileceğinden templates ve static klasörlerimizin path lerini kendimiz prmetre olarak belirlemek zorundayız aksi halde Blueprint den oluşturuğumuz objelerimiz bu klasörleri bulamayacaktır.

--- 
## Flask ile Veritabanı Bağlantısı
Flask, PostgreSQL, SQLite ve MySQL gibi RDBMS'lerin çoğuyla çalışır. Ancak veritabanlarına bağlanmak için 'Flask-SQLAlchemy' uzantısını(paket) kullanmalıyız.
SQL sorguları yazmaya gerek kalmadan geliştirme sırasında veritabanı etkileşimini ve yönetimini kolaylaştırır.Ayrıca, SQL enjeksiyon saldırılarına eğilimlidir. 
MongoDB gibi No-SQL veri depolarıyla çalışmak için ise 'Flask-MongoEngine' uzantısını kullanabiliriz.

---
## Flask ve SQLite
SQLite, Python içind gömülüdür. Veritabanını Flask'ta kullanmak için herhangi bir ek Flask Uzantısı yüklememize gerek yoktur. Uygulamamız içinde, SQLite'ı içe aktarabilir ve veritabanıyla etkileşim için SQL sorguları yazabiliriz. <br>
Bağlantıyı yapmak için config ayarını yapmamız yeterli. Config ayarlarını istersek uygulamızda oluşturduğumuz Flask nesnesine yazabiliriz yada istersek uygulamamızın bulunduğu klasörde config.py adlı bir dosya oluşturup <object>.from_pyfile('config.py') metotu ile bağlantıyı sağlayabiliriz. <br>
**app.py**
```
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///deneme.db'
```
**config.py**
```
SQLALCHEMY_DATABASE_URI = 'sqlite:///deneme.db'
```
---

## Jinja2 Template Sayfaları
- [Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) hızlı, etkileyici, genişletilebilir bir şablon oluşturma motorudur. Şablondaki özel yer tutucular, Python sözdizimine benzer kod yazmaya izin verir. 
Özet olarak belirtmek gerekirse bu python kodları '{{ }}' ve '{% %}' arasındaki kısımlarda gerçekleşmekte. Daha doğru bir söylem ile bu kısımlarda oluşturduğumuz değişken isimleri projemizin python kısmında çalışıyor ve sonuçlar bu kısımlara aktarılmakta ve uygulamamız içinde bu sonuçlar gösterilebilmektedir.
---

## Template Kalıtımı(Inheritance)
Jinja'nın en güçlü yanlarından biri template(şablon) inheritance dır. Şablon kalıtımı, sitenizin tüm ortak öğelerini içeren ve alt şablonların geçersiz kılabileceği blokları tanımlayan bir temel "iskelet" şablonu oluşturmanıza olanak tanır.
<br>
Kulağa karmaşık geliyor ama çok basit. Bir örnekle başlayarak anlamak en kolayı.
### Base Template 
'layout.html' yada 'base.html' olarak adlandırabileceğimiz bu şablon, basit bir sayfa için kullanabileceğiniz basit bir HTML iskelet belgesini tanımlar. Boş blokları içerikle doldurmak "alt" şablonların işidir:
```
<!doctype html>
<html>
  <head>
    {% block head %}
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
    <title>{% block title %}{% endblock %}</title>
    {% endblock %}
  </head>
  <body>
    <div id="content">{% block content %}{% endblock %}</div>
    <div id="footer">
      {% block footer %}
      &copy; Copyright 2023 by <a href="http://domain.invalid/">you</a>.
      {% endblock %}
    </div>
  </body>
</html>
```
Bu örnekte, {% blok %} etiketleri, alt şablonların doldurabileceği dört blok tanımlar. Blok etiketinin yaptığı tek şey, şablon motoruna bir alt şablonun şablonun bu bölümlerini geçersiz kılabileceğini söylemektir.
Özetle ilk başta ana HTML sayfası yüklenir ve kalıtımı alacağımız HTML sayfasında {% block x %}{% endblock %} arasını diğer html sayfalarında aynı block işaretlemesini yaparak aralarını doldururuz ve override yaparız.
Daha iyi anlamak için kalıtım aldığımız child şablonda inceleyelim.

### Child Template
```
{% extends "layout.html" %}
{% block title %}Index{% endblock %}
{% block head %}
  {{ super() }}
  <style type="text/css">
    .important { color: #336699; }
  </style>
{% endblock %}
{% block content %}
  <h1>Index</h1>
  <p class="important">
    Sayfama Hoşgeldiniz.
{% endblock %}
```
{% extends %} etiketi burada anahtardır. Şablon motoruna child şablon yüklenirken parent üzerinden yüklenmesini belirtir. Şablon sistemi bu şablonu render ederken önce base şablonu bulur. Extends etiketi, şablondaki ilk etiket olmalıdır. Ana şablonda tanımlanan bir bloğun içeriğini kullanmak istiyorsanız {{ super() }} kullanabilirsiniz.

### Include

Özellikle çok sayfalı siteler yaparken header, footer, nav gibi bölümleri defalarca kullanıyoruz. include sayesinde farklı bir HTML sayfasında bu bölümleri yazıp şablonumuza dışarıdan dahil ederek aynı bölümleri yazmayı önlüyoruz.
<br>
**'header.html'**
```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Templates</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
<div class="header">
    <h1>{{ baslik }}</h1>
</div>
```
<br>
  
**'footer.html'** <br>
  
```
<footer>
    <h2> © Copyright XXX 2023</h2>
</footer>

</body>
</html>
```

2 Adet include edeceğimiz sayfamızı oluşturduk. Şimdi istediğimiz şablonlarımızda bu header ve footer bölümünü çağırabiliriz ve uygulamamızı kod kalabalığından uzak tutabiliriz.

```
{% include 'header.html' %}

<div class="list">
    <img align='left' src="../static/images/flask.png" alt="flask">
    <ul align="center">
        <li>{{ degisken1 }}</li>
        <li>{{ degisken2 }}</li>
        <li>{{ degisken1+degisken2 }}</li>
    </ul>
</div>

{% include 'footer.html' %}
```
<br>



HTML sayfası içinde değişken kullanımı:
```
{{ variable }}
```
HTML sayfası içinde koşullu ifadele kullanımı:
```
{% if variable %}
{{ variable }}
{% endif %}
```
HTML sayfsı içinde loop kullanımı:
```
{% for data in list %}
{{ data }}
{% endfor %}
```
---

## Default Host ve Port
Flask uygulamamızın varsayılan:
- Host: http://.27.0.0.1
- Port: 5000
Fakat bunu uygulamamız içinden değiştirebiliyoruz.
```
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
```

---
## Basit Flask Uygulaması
Flask ile yapacağımız web uygulamamızın en önemli kısımlarından biri varsayılan host ve porta (http://localhost:5000) client üzerinden gelecek olan requestlere response döndüren python dosyamızdır. Kısaca Flask sınıfından objemizi initialize edeceğimiz python dosyasıdır diyebiliriz.
**app.py**
```
from flask import Flask
```
Flask sınıfımızı import etmekle başlıyoruz.
```
app = Flask(__name__)
```
Flask sınıfından bir 'app' nesnesi oluşturuyoruz.
```
@app.route('/')
def index():
    return '<h1>Hello World</h1>'
```
Çalıştırmak için python dosyamızın ismi app.py ise bulunduğu klasörde terminal açıp
```
flask --app run
```
yada
```
flask run
```
yazmamız yeterlidir. Lakin dosyanın ismi farklı ise
```
flask --app <dosyaismi> run
```
yazılmalıdır.

![flaskrun](https://user-images.githubusercontent.com/120065120/212184085-f9ad83ae-8c1a-4f93-a218-59235b6da660.PNG)

index() fonksiyonumuz da route() decoratorunu gelen requestlere fonksiyonumuzun bir cevap döndürmesi için kullanıyoruz. Fonksiyonumuz 'return' ile bir değer döndürmelidir. route() metodu parametre olarak bir endpoint alıyor ve bizim burda kullandığımız '/' anasayfamızı temsil ediyor.
Özetle anasayfamıza('/') bir GET request atıldığı zaman fonksiyonumuz tetikleniyor ve cliente bir response yolluyor.

![index](https://user-images.githubusercontent.com/120065120/212183376-3c1add42-399b-4957-b60b-50c30cd65b7d.PNG)

**ÖZET**
1. İlk önce Flask sınıfını importladık. Bu sınıftan oluşturduğumuz nesne bizim WSGI uygulamamız olacaktır.
2. Daha sonra bu sınıfın bir örneğini oluşturuyoruz. İlk parametremiz, uygulamanın modülünün veya paketinin adıdır. __name__, ile bunu kısa bir şekilde halledebiliyoruz. Bu, Flask'ın templates ve static dosyalar gibi kaynakları nerede arayacağını bilmesi için gereklidir.
3. Ardından, Flask'a hangi URL'nin işlevimizi tetiklemesi gerektiğini söylemek için route() dekoratörünü kullanıyoruz.
4. Fonksiyon, clientin tarayıcısında görüntülemek istediğimiz mesajı döndürür. Varsayılan response türü HTML'dir.
---

## Route Deişkenleri

Flask, uygulamamızda URL mize değişken ekleyerek dinamik hale getirmemizi mümkün kılıyor. Bu değişkenimizi URL mizde route('/<değişken>') olarak kullanabiliriz ve decoratorumuzun kullanıldığı fonksiyonda bu değişkeni çağırabiliriz.

## HTTP Metotları

Web uygulamaları, URL'lere erişirken farklı HTTP yöntemleri kullanır. Flask ile çalışıyorsanız eğer HTTP yöntemlerine aşina olmalısınız. Default olarak, route() yalnızca GET isteklerine yanıt verir. Farklı HTTP yöntemlerini işlemek için route() dekoratörünün 'methods' parametresini kullanarak diğer metotları da URL'miz de işlenecek hale getirebilirsiniz.
```
@app.route('/login', methods=['GET', 'POST'])
```
![HTTP](https://user-images.githubusercontent.com/120065120/212473876-ec278681-1d26-460a-952b-6f0fe7898e47.png)


```
from flask import request

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
```

- **GET**: Bu metod ile sunucudan veri alınabilir. GET ve POST metodları genel olarak en sık kullanılan metodlar olup sunucudaki kaynaklara erişmek için kullanılırlar.GET metodu ile sorgu metinleri URL içinde gönderilebilir. Bunun en önemli faydası kullanıcıların bookmark edebilmeleri ve aynı sorguyu içeren istekleri daha sonra gönderebilmelerini sağlaması ve tarayıcıda önceki sorguların “geri” tuşu ile veya tarayıcı geçmişinden çağrılarak aynı sayfalara ulaşabilmeleridir. Güvenlik açısından URL’lerin ekranda görüntüleniyor olması ve URL’in hedefine ulaşıncaya kadar ve hedef sunucu üzerinde iz kayıtlarında görülebilmesi gönderilen parametrelerin gizlilik ihtiyacı varsa sıkıntı yaratabilir. Bu nedenlerle hassas isteklerin GET ile gönderilmemelidir.
- **POST**: Bu metod ile sunucuya veri yazdırabilirsiniz. Bu metodla istek parametreleri hem URL içinde hem de mesaj gövdesinde gönderilebilir. Sadece mesaj gövdesinin kullanımı yukarıda sayılan riskleri engelleyecektir. Tarayıcılar geri butonuna basıldığında POST isteğinin mesaj gövdesinde yer alan parametreleri tekrar göndermek isteyip istemedimizi sorarlar. Bunun temel nedeni bir işlemi yanlışlıkla birden fazla yapmayı engellemektir. Bu özellik ve de güvenlik gerekçeleriyle bir işlem gerçekleştirileceğinde POST metodunun kullanılması önerilir.
- **DELETE**: Bu metod ile sunucudaki herhangi bir veriyi silebilirsiniz.
- **PUT-PATCH**: Bu metodlar bir kaynakta istediğiniz değişimi yapmanızı sağlar.PATCH'in PUT'tan temel olarak farkı daha küçük çaplı değişim yapmasıdır.

---

## Flask ve Unique URL'ler

Aşağıdaki iki kural, sondaki eğik çizgi kullanımlarında farklılık gösterir.

```
@app.route('/projeler/')
def projects():
    return 'Proje Sayfası'

@app.route('/hakkinda')
def about():
    return 'Hakkında Sayfası'
```

- '/projeler/' endpointi için standart URL'de sonunda bir slash(eğik çizgi) var URL'ye sonunda slash (/projeler) olmadan erişirseniz, Flask sizi sonunda eğik çizgi (/projects/) bulunan standart URL'ye yönlendirir.
<br>
- '/hakkinda' URL'mizin bitiş noktasında slash yoktur.URL'ye slash ile (/about/) erişildiği zaman 404 "Not Found" hatası oluşacaktır. Bu, URL'lerin benzersiz kalmasına ve arama motorlarının aynı sayfayı iki kez dizine eklemekten kaçınmasına yardımcı olur.
---








