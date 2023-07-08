## Flask - Dosya Yapısı

Genel olarak uygulamalarımızı hep 1 yada 2 adet python dosyası üzerinden yürüttük(main.py-forms.py gibi).Fakat uygulamamız büyüdükçe kod karışıklığı ve maliyet oldukça artacaktır.
Python bize oldukça readable bir kod mantığı sağlarken de işleri karıştırmanın hiç lüzumu yok. Özellikle Flask gibi esnek ve basit bir framework kullanıyorsak bu bizim isteyeceğimiz son şey olabilir. 😊

- Büyük ölçekli Flask uygulamaları için uygulamanın bölümlerini kendi dosyalarına ayırmak daha mantıklıdır.(models.py, forms.py, views.py)
- Daha da büyük ölçekli Flask uygulamaları için tüm bu bileşenleri kendi klasörleri içinde tutmak ise bize oldukça kolaylık sağlayacaktır.(Forms, Models, Templates, Static, Views vb.)


[Mini Proje](https://github.com/erkamesen/Flask-Rehber/tree/main/Flask%20-%20Database/Mini%20Proje) miz üzerinden yola çıkarak re-structure yaparsak eğer;

- app.py dosyamızı 2 adet bileşe ayırabiliriz.
1. Dogs
2. Owners
   
- Hatta **blueprints** kütüphanesini kullanarak ayırdığımız tüm bu bileşenleri app.py dosyamızda birleştirebiliriz.
- Önemli !!! app.py dosyası silinmeyecek.Tüm bu bileşenleri app.py üzerinden birleştireceğimiz için diğer oluşturduğumuz componentlere referans olarak bu dosyayı kullanıcaz.
  

## Örnek DOSYA YAPISI

├── **app.py** > *Uygulamayı başlatcağımız ana dosyamız.*
├── **requirements.txt** > *pip ile kurulacak dosyalar.*
├── **migrations** > *Migrations kurulumu yaptıktan sonra oluşacak klasör.*
├── **myproject** > *Main proje dosyası, componentler bunun içinde olucak.*
&nbsp;|&emsp;&emsp;|  **data.sqlite**
&nbsp;|&emsp;&emsp;|  **models.py**
&nbsp;|&emsp;&emsp;|  **\_\_init__.py**
&nbsp;|&emsp;&emsp;|
&nbsp;|&emsp;&ensp; ├─ **Owners**
&nbsp;|&emsp;&emsp;|&emsp;&emsp;&nbsp;| **forms.py**
&nbsp;|&emsp;&emsp;|&emsp;&emsp;&nbsp;| **views.py**
&nbsp;|&emsp;&emsp;|&emsp;&emsp;&nbsp;|
&nbsp;|&emsp;&ensp; &nbsp;|&emsp;&emsp;├─ **templates**
&nbsp;|&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├ **owners**
&nbsp;|&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├ **add_owner.html**
&nbsp;|&emsp;&emsp;|
&nbsp;|&emsp;&emsp;|
&nbsp;|&emsp;&ensp; ├─ **Dogs**
&nbsp;|&emsp;&emsp;|&emsp;&emsp;&nbsp;| **forms.py**
&nbsp;|&emsp;&emsp;|&emsp;&emsp;&nbsp;| **views.py**
&nbsp;|&emsp;&emsp;|&emsp;&emsp;&nbsp;|
&nbsp;|&emsp;&ensp;&nbsp;&nbsp;|&emsp;&emsp;├─ **templates**
&nbsp;|&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├ **dogs**
&nbsp;|&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├ **add.html**
&nbsp;|&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├ **delete.html**
&nbsp;|&emsp;&emsp;|&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;├ **list.html**
&nbsp;|&emsp;&emsp;|
&nbsp;|&emsp;&ensp; ├─ **static** > *CSS, JS, resim dosyaları gibi statik dosyalarının olduğu klasör.*
&nbsp;|&emsp;&ensp; ├─ **templates**
&nbsp;|&emsp;&ensp;&emsp;&nbsp;&emsp;&nbsp; ├─ **base.html**
&nbsp;|&emsp;&ensp;&emsp;&nbsp;&emsp;&nbsp; ├─ **home.html**

## Re-Structure

- Re-structure yapılmış Flask uygulamamızın genel yapısını inceledik, şimdi sıra uygulamımızı bu formata göre şekillendirmeye geldi.

- Flask componentleri ayırmak ve belli dosyalar üzerinde bağlantılarını sağlamak için built-in olarak *blueprints* özelliğine sahiptir.
- Bu yol ile beraber kolayca componentlerimizin **view** dosyalarını ayırabiliriz.
- Örnek olarak 2 adet views.py dosyamız olsun.Bir tanesi **owners** için diğeri ise **dogs** için.
- Her iki views.py dosyamızda da **add** view i olsun
- Flask uygulamamızın bu /add view lerini karıştırmaması için blueprints kullanıyoruz.
- Blueprints in url_prefix() metodu ile /end viewlarını componentlere göre kaydedersek alacağımız olası sonuç:
1. /owners/add
2. /dogs/add
- [Mini Proje](https://github.com/erkamesen/Flask-Rehber/tree/main/Flask%20-%20Database/Mini%20Proje) bu kod arasındaki en temel farklar:

1. Projenin dosya yapısı tamamen değişti.
2. Blueprints ler eklendi
3. Blueprints ler \__init__.py üzerinde register edildi.
   
> Proje boyunca hataya neden olacak basit bir yazım hatası yapmak çok kolay olacağından dikkat edilmesi önemlidir.

> Bu yapı [Mini Proje](https://github.com/erkamesen/Flask-Rehber/tree/main/Flask%20-%20Database/Mini%20Proje) üzerinden copy/paste yapılarak kurulmuştur.


