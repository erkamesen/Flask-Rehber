from flask import Flask, jsonify

app = Flask(__name__)  # Flask sinifindan app adinda bir nesne uretiyoruz.

"""
Çalıştırmak için dosyanın bulunduğu klasörde terminal açıp 
'flask run' yazbilirsiniz.
"""


# '/' route umuza GET request geldigi zaman cliente
# <h1> tagında 'Hello World' yazısı ile bir HTML file döndürüyoruz.

@app.route('/')  # http://127.0.0.1:5000/
def index():
    return '<h1>Hello World</h1>'


# Farklı bir URL için bir fonksiyon oluşturduk ve bu URL ye istek geldiği zaman
# Altındaki fonksiyon tetiklenerek cevap oluşturucak.

@app.route('/goodbye')  # http://127.0.0.1:5000/goodbye
def bye():
    return '<h1> Goodbye World :( </h1>'


# Dinamik URL oluşturmak için <degisken> imizi URL den alıp fonksiyonda işlemek için
# parametre olarak veriyoruz. Bu sayede işleyip değişkene göre bi response döndürebiliyoruz.
# <int:degisken> -- <string:degisken> -- <float:degisken> -- <path:degisken> ile
# değişkenin tipini belirleyebiliyoruz.

@app.route('/hello/<string:user>')  # http://127.0.0.1:5000/hello/<degisken>
def helloUser(user):
    if user == 'admin':  # Ayrıca css kodlarımızı da buraya yazabiliyoruz.
        return '<h1 align="center" style="color:red;" >Hoşgeldin Sahip</h1>'
    else:
        return f'<h1>Hello {user}</h1>'

# Flask uygulamalarında defult olarak methodumuz GET olduğu gibi default olarak
# response döndürürken HTML dosyası yollarız jsonify() yada make_response() ile bunu
# değiştirebiliriz. Aşağıda jsonify() ile json_data adında oluşturduğum sözlüğü JSON olarak
# iletiyorum.


@app.route('/json')
def notHTML(): # http://127.0.0.1:5000/json
    json_data = {'a': 1,
                 'b': 2,
                 'c': 3}
    return jsonify(json_data)


if __name__ == '__main__':
    app.run()