## Flask Login

### Hashing

- Uygulamamıza kullanıcılar kayıt olduktan sonra bize verilen bilgileri veritabanımızda tutmak zorundayız.
- Önemli bilgileri Text formatında tutmak güvenlik açısından büyük sorun doğuracağından asla bu şekilde tutmamalıyız.
- Eğer Text formatında tutarsak sitemize olası bi saldırı sonucu art niyetli kişilerin elde edeceği veriler tam da kucaklarına düşecektir.
- Bunun önüne geçmek için hash fonksiyonunu kullanabiliriz.

> [Hash fonksiyonu](https://metatime.com/tr/blog/hash-fonksiyonu-hash-function-nedir) (Hash Function), verileri sabit uzunluktaki farklı bir değere çeviren matematiksel işlemler olarak bilinir. Hash fonksiyonları genel olarak bir verinin bütünlüğünü korumak adına kullanılır. İşlemin sonucunda alınan çıktıya ise hash değeri veya hash kodu ismi verilir. Hash değeri, verilerin bütünlüğünü korumada yardımcı olur. Hash fonksiyonlarının önemli özelliklerinden biri, aynı girdiler için her zaman aynı hash değerini üretmeleridir. Farklı girdiler içinse farklı hash değerleri çıkarırlar. Tüm bunlardan dolayı hash fonksiyonları, güvenliği sağlamak ve veri bütünlüğünü korumak amaçlı sıklıkla kullanılır.

- Hash Ornek klasöründen *werkzeug* ve *bcrypt* library leri ile yapılmış örnekleri görebilirsiniz.

### Flask-Login

```
pip install flask-login
```

- Flask-Login kütüphanesi web uygulamamızın kimlik doğrulama işlemlerini basit bir şekilde halletmek için oluşturulmuştur.
- Sağladığı decoratorler ile sadece kullanıcılara özel view ları oluşturmanızı sağlar.(Giriş yapılmadan görülmeyen sayfalar vb.)

