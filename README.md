# Flask-Rehber

![1 0G5zu7CnXdMT9pGbYUTQLQ](https://user-images.githubusercontent.com/120065120/212087425-6ee72546-16fc-476a-9067-54de6a4efbd9.png)

İçerik:
1. [Flask Nedir ?](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#flask-nedir-)
2. [WSGI Nedir ?](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#wsgi-nedir-)
3. [Flask Kurulumu](https://github.com/erkamesen/Flask-Rehber/edit/main/README.md#flask-kurulumu)
--- 

## Flask Nedir ?

En kısa hali ile Flask 2011 yılında Pocoo python topluluğundan 'Armin Ronacher' tarafından nisan şakası olarak çıkarılan, python dili ile yazılmış açık kaynak bir web geliştirme micro framework'üdür.(Web Framework).
Flask çabuk öğrenilebilen, kolay ve ihtiyacımız olan ek paketleri sonradan projemize dahil edebildiğimiz için projenin hantallaşmasını önleyen, route yapısı basit ve bencmarklarına bakıldığında performansı gayet yüksek bir frameworktür.
Python kodlarını yazmak için Django gibi Jinja2 şablon motorunu ve Werkzeug aracı ile WSGI arayüzünü kullanır.

- [Flask](https://flask.palletsprojects.com/en/2.2.x/)
- [Pocoo](https://www.pocoo.org/)

## WSGI Nedir ?

WSGI (Web Server Gateway Interface-Web Sunucusu Ağ Geçidi Arayüzü) python ile bir web uygulaması geliştirmek için kullanılan arayüzdür. Server olarak da adlandırılabilir.Web Server'ların python kodumuzu anlaması için bize aracılık eder. Sonuç olarak eğer WSGI kullanmazsak server yazdığımız kodları çalıştıramayacaktır.

## Flask Kurulumu

Windows:
```
pip instll flask
```
Linux-Mac:
```
pip3 instll flask
```
## Klasör Yapısı

/project
        /templates/
                   index.html
                   sayfa2.html
                   sayfa3.html
        /static/
              main.css
        /app.py

Flask uygulamamızda Flask sınıfından objemizi initialize ettiğimiz .py dosyamızın içinde bulunduğu klasör içindeki: 
- /templates klasörü içine HTML dosyalarımızı oluşturuyoruz.
- /static klasörü içinde CSS , assets , resim dosyalarımızı  oluşturuyoruz.
Bu yapı objemizi oluşturduğumuz python dosyasına göre default şekilde ayarlıdır ve dileğe göre obje oluşturulurken parametre olarak path değiştirilebilir.(-zorda kalmdıkça tavsiye edilmez-) Özellikle Blueprint le çalışırken blueprintlerimizi views klasörü içinde oluşturulabileceğinden templates ve static klasörlerimizin path lerini kendimiz prmetre olarak belirlemek zorundayız aksi halde Blueprint den oluşturuğumuz objelerimiz bu klasörleri bulamayacaktır.
