## HTML Forms

## 'form.html'
![Seçim_025](https://user-images.githubusercontent.com/120065120/214096736-907e13ae-11fc-42bd-a1f3-ce24461f9f13.png)

**form.html**
```
<form method="post" action="{{url_for('forms')}}">
<input type="text" class="form-control mb-2" id="inlineFormInput" placeholder="Erkam Esen" name="isim">
<input type="email" class="form-control" id="exampleFormControlInput1" placeholder="name@example.com" name="email">
<select class="form-control" id="exampleFormControlSelect1" name="porsiyon">
</form>
```
Kısa şekilde yazdığım form.html de oluşturulan bu formda **{{url_for('forms')}}** yardımı ile bilgilerimizi forms() fonksiyonuna yolluyoruz.(Aslında zaten
forms() fonksiyonundan geldiğimiz için bu default olarak geldiğimiz fonksiyon olacağından yazmamıza gerek yoktu ama action="" ile hangi fonkisyona bilgileri 
yolladığımızı bilin yeterli.)

inputlarımızın name="" parametrelerini fonksiyonumuzda yakalayacağımızdan onlara içerikleriyle benzer ve farklı şeyler veriyoruz.

**app.py**
```py
@app.route("/html-form", methods=["GET", "POST"])
def forms():
    if request.method == "POST":
        isim = request.form.get("isim")
        email = request.form.get("email")
        porsiyon = request.form.get("porsiyon")
        malzemeler = request.form.getlist('check')
        adres = request.form.get("adres")
        odeme = request.form.get("odeme")
        siparis = {
            "isim": isim,
            "email": email,
            "porsiyon": porsiyon,
            "malzemeler": malzemeler,
            "odeme": odeme,
            "adres": adres
        }
        return render_template("result.html", **siparis)
    return render_template("form.html")
```
Formumuzun olduğu sayfa, formumuzdan methodumuz POST olacağı için route umuza bunu belirtiyoruz.
endpointler default olarak sadece GET request alıyolar farklı methodlar için belirtmek gerekiyor.
request.method == 'POST' ile isteği yakalıyoruz.
request.form.get('') ile HTML formundan name yerine yazdıklarımızı fonksiyonumuza çekiyoruz.
siparis adında bir dict() oluşturup **siparis ile bunu result.html sayfasına yolluyoruz.


## 'result.html'
![Seçim_026](https://user-images.githubusercontent.com/120065120/214096744-30ea1fae-9bb5-4371-b676-c0b917570b24.png)

```
 <h1>Siparişiniz Oluşturuldu</h1>
    <p>İsim: {{ isim }}</p>
    <p>Email: {{ email }}</p>
    <p>Porsiyon: {{ porsiyon }}</p>
    <p>Malzeme: {% for malzeme in malzemeler %}
        {{ malzeme | capitalize}}
        {% endfor %}</p>
    <p>Ödeme Türü: {{ odeme }}</p>
    <p>Adres: {{ adres }}</p>
```
**siparis ile HTML sayfamıza işlemek için yolladığımız değişkenlerimizi teker teker yakalıyoruz.
Ayrıca malzemeler kısmını getlist() olarak aldığımız için elimizde bir liste var bu sebeple for loopuna alıp malzemelerimizi tek bir <p> tagına düzgünce yerleştiriyoruz.
  | capitalize filtresi ile ise baş harflerini büyütüyoruz.


