from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)

"""
index.html de oluşturduğumuz header var1 ve var2 değişkenlerini
{{ degisken1 }} {{ degisken2 }} ve {{ baslik }} kısmında işlemek için
renderlayacağımız HTML sayfasına yolluyoruz.
"""


@app.route('/')
def index():
    header = 'Flask Templates'
    var1 = 4
    var2 = 16
    return render_template('index.html', baslik=header, degisken2=var2, degisken1=var1)


#############################################################################

"""
for loop da {% for var in list %} {% var %} {% endfor %}
şeklinde aynı mantıkla iterable verileri işleyebiliyoruz.
Burda işlemek için for.html şablonuna listyi ve include da
tekrar kullanacağımız için baslik i yolluyoruz.
"""


@app.route('/forloop')
def forloop():
    team_list = ['muslera', 'chedjou', 'semih', 'telles', 'eboue',
                 'melo', 'selcuk', 'sneijder', 'riera', 'drogba', 'burak']
    return render_template('for.html', baslik='For Loop', team=team_list)


#############################################################################


"""
if-elif-else durumları için for loopunda olduğu gibi kodlarımızı {% %} arasına yazıyoruz.
bu örneğimizde yine bir liste yolladık ve şablon içinde {% if 'muslera' in team %}
ile listenin içini kontrol ediyoruz. {% else %} yaa {% elif .... %} ile farklı durumları
kontrol edebiliriz. En son {% endif %} ile bitiriyoruz. Özellikle giriş ypılan uygulamalarda
is_login değişkenine True False değeri verip giriş yapım durumuna göre şablonumuzdan veriler
gösterebiliyoruz.
"""


@app.route('/ifelse')
def ifelse():
    team_list = ['ismailcipe', 'chedjou', 'semih', 'telles', 'eboue',
                 'melo', 'selcuk', 'sneijder', 'riera', 'drogba', 'burak']

    return render_template('if.html', baslik='If - Elif - Else', team=team_list)


#############################################################################

"""
context_processor decoratoru ile de uygulamamıza data yollayabiliyoruz.
Burda Copyright kısmı için dinamik bir yıl verisi yolluyoruz.
"""

from datetime import datetime


@app.context_processor
def index():
    current_year = datetime.now().year
    return {'year': current_year}
