# Flask-Rehber

![1 0G5zu7CnXdMT9pGbYUTQLQ](https://user-images.githubusercontent.com/120065120/212087425-6ee72546-16fc-476a-9067-54de6a4efbd9.png)

İçerik:
- [Flask Nedir ?](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#flask-nedir-)
- [Flask Dependencies(Bağımlılıklar)](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#flask-dependenciesba%C4%9F%C4%B1ml%C4%B1l%C4%B1klar)
- [WSGI Nedir ?](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#wsgi-nedir-)
- [Werkzeug Nedir ?](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#werkzeug-nedir-)
- [Flask Kurulumu](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#flask-kurulumu)
- [Klasör Yapısı](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#klas%C3%B6r-yap%C4%B1s%C4%B1)
- [Jinja2 Template Sayfaları](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#jinja2-template-sayfalar%C4%B1)
- [Default Host ve Port](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#default-host-ve-port)
- [Basit Flask Uygulaması](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#basit-flask-uygulamas%C4%B1)
- [Route Değişkenleri](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#route-dei%C5%9Fkenleri)
--- 

## Flask Nedir ?

En kısa hali ile [Flask](https://flask.palletsprojects.com/en/2.2.x/) 2011 yılında Pocoo python topluluğundan 'Armin Ronacher' tarafından nisan şakası olarak çıkarılan, python dili ile yazılmış açık kaynak bir web geliştirme micro framework'üdür.(Web Framework).
Flask çabuk öğrenilebilen, kolay ve ihtiyacımız olan ek paketleri sonradan projemize dahil edebildiğimiz için projenin hantallaşmasını önleyen, route yapısı basit ve benchmarklarına bakıldığında performansı gayet yüksek bir frameworktür.
Python kodlarını yazmak için Django gibi Jinja2 şablon motorunu ve Werkzeug aracı ile WSGI arayüzünü kullanır.


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
## Jinja2 Template Sayfaları
[Jinja2](https://jinja.palletsprojects.com/en/3.1.x/) hızlı, etkileyici, genişletilebilir bir şablon oluşturma motorudur. Şablondaki özel yer tutucular, Python sözdizimine benzer kod yazmaya izin verir. 
Özet olarak belirtmek gerekirse bu python kodları '{{ }}' ve '{% %}' arasındaki kısımlarda gerçekleşmekte. Daha doğru bir söylem ile bu kısımlarda oluşturduğumuz değişken isimleri projemizin python kısmında çalışıyor ve sonuçlar bu kısımlara aktarılmakta ve uygulamamız içinde bu sonuçlar gösterilebilmektedir.

HTML sayfası içinde değişken kullanımı:
```
{{ deşişken }}
```
HTML sayfası içinde koşullu ifadele kullanımı:
```
{% if degisken %}
{{ deşişken }}
{% endif %}
```
HTML sayfsı içinde loop kullanımı:
```
{% for i in degisken %}
{{ i }}
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
---

## Route Deişkenleri

Flask, uygulamamızda URL mize değişken ekleyerek dinamik hale getirmemizi mümkün kılıyor. Bu değişkenimizi URL mizde route('/<değişken>') olarak kullanabiliriz ve decoratorumuzun kullanıldığı fonksiyonda bu değişkeni çağırabiliriz.









