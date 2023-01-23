from flask import Flask, render_template, request
app = Flask(__name__)



# Anasayfamız
@app.route('/')
def index():
    return render_template('index.html')


# Formumuzun olduğu sayfa, formumuzdan methodumuz POST olacağı için route umuza bunu belirtiyoruz.
# endpointler default olarak sadece GET request alıyolar farklı methodlar için belirtmek gerekiyor.
# request.method == 'POST' ile isteği yakalıyoruz.
# request.form.get('') ile HTML formundan name yerine yazdıklarımızı fonksiyonumuza çekiyoruz.
# siparis adında bir dict() oluşturup **siparis ile bunu result.html sayfasına yolluyoruz.
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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
