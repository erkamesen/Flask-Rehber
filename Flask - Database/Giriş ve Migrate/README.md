## Flask - SQL


### Başlarken

SQL sorgularını kendi öz dilinde yazmaktan ziyade ORM(Object Relational Mapper) kullandık. Bu sayede sorgularımızı "Python" syntax i kullanarak yapıyoruz. <br>
Temel olarak mantık SQL içerisinde bir tablo ile python üzerinde oluşturduğumuz bir "Class" ın ilişkilendirilmesi diyebiliriz. Bu sayede oluşturduğumuz sınıftan ürettiğimiz objeler ve metotları ile SQL sorgularımızı rahatça yapabiliyoruz.
<br>
Python için en popüler ORM olan SQLAlchemy kullanıcaz.Direkt olarak "Flask-SQLAlchemy" extension ını kurmak için aşağıdaki kodu komut satırına yazabilirsiniz.

```
pip install Flask-SQLAlchemy
```

### Adımlar

Veritabanları ile çalışmaya başlamadan önce takip edeceğimiz adımlar:

1. *Flask uygulamamız üzerinde SQLite kurulumu.*
2. *Flask uygulamamız üzerinde "Model" oluşturma.*
3. *Oluşturduğumuz model üzerinden temel CRUD işlemlerinin yapımı.*



#### Flask uygulamamız üzerinde SQLite kurulumu

- *Bir Flask uygulaması oluşturma.*
- *Flask uygulamamız içerisinde SQLAlchemy için config ayarlarını yapmak.*
- *SQLAlchemy nesnesini Flask uygulaması içerisinde çağırma ve initialize etme.*

#### Flask uygulamamız üzerinde "Model" oluşturma.

- *Modeller direkt olarak SQL veritabanındaki tablolar ile bağlanır.*
- *SQL üzerinden tablo oluşturmaya gerek kalmıyor*
- *Python ile oluşturduğumuz Model Class ı ile basit bir şekilde bağlantıyı yapabiliyoruz.*

Model Oluşturma:
- *Bir adet Model Classı oluştur.*
- *"db.Model" Sınıfını miras olarak alın.*
- *Opsiyonel olarak bir tablo ismi sağlayın.*
- *Tabloda ki kolonları Class attribute ları ile oluşturun.*

#### Oluşturduğumuz model üzerinden temel CRUD işlemlerinin yapımı.

Temel CRUD işlemlerini ele alıcaz:

- *C - Create*
- *R - Read*
- *U - Update*
- *D - Delete*


## Flask - Migrate

- Veritabanı tablosu için bir model oluştururken, bazen modelde yeni bir kolon eklemek gibi ayarlamalar yapmanız gerekecektir.
- Bu değişiklikleri yaptıktan sonra, veritabanı tablosunu güncellemek için bu değişiklikleri "migrate" yapmanız gerekecek.
- Flask üzerinde migrate yapmak için "Flask-Migrate" extension ını kullanabiliriz.
```
pip install Flask-Migrate
```
- Bu extension ile Model class ımızda ayarlar yapmamızı ve ardından bu ayarların SQL Database inde de etkili olduğundan emin olmamızı sağlar.
- Terminal üzerinden kullanabileceğimiz 4 temel komut vardır :

1. *FLASK_APP env değişken ayarı:*
- MacOS/Linux
```
export FLASK_APP=app.py
``` 
- Windows
```
set FLASK_APP=app.py
```
Eğer flask app  env değişkenini ayarlamadıysanız aşağıdaki hatayı alabilirsiniz:
> Error: Cold not locate Flask application. You did not provide FLASK_APP environment variable.

"migrations_instructions.txt" Dosyasını kontrol edebilirsiniz.

2. Migrations klasörünü ayarlama

```
flask db init
```
3. Migrations klasörünü ayarlama

```
flask db migrate -m "mesaj"
```

4. Veritabanını migration ile birlikte güncelleme

```
flask db upgrade
```

"basic.py" içerisinde Model Class ımızı oluştururken migrate yapmadan önce sadece id, name ve age kolonu vardı fakat sistem büyüyünce ihtiyaçları değişti ve "breed" adında yeni bir kolon eklemek zorunda kaldık. Bunu da Flask-Migrate ile 3. ve 4. komutları kullanarak çok rahat şekilde hallettik.

