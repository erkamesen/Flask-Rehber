from models import db, Dog, Toy, Owner, app

# 2 ADET KÖPEK OLUŞTURMA

with app.app_context():
    rufus = Dog("Rufus")
    fido = Dog("Fido")

    # Köpekleri veritabanına ekleme
    db.session.add_all([rufus, fido])

    # Commitleme
    db.session.commit

    # Kontrol
    print(Dog.query.all())
    # [Köpegin adi Rufus ve henüz bir sahibi yok!, Köpegin adi Fido ve henüz bir sahibi yok!]


    # Rufusu çağırıyoruz
    rufus = Dog.query.filter_by(name="Rufus").first() # .all() liste olarak getirdiği için .first() kullanıyoruz

    # Sahip oluşturma
    erkam = Owner("Erkam", rufus.id) # Rufusun ID sini veriyoruz.

    # Rufusa oyuncak verelim

    toy1 = Toy("Kemik", rufus.id)
    toy2 = Toy("Top", rufus.id)

    # Oluşturulan verileri ekleme
    db.session.add_all([erkam, toy1, toy2])
    db.session.commit()

    # Kontrol
    rufus = Dog.query.filter_by(name="Rufus").first()
    print(rufus)
    # Köpegin adi Rufus ve sahibinin adi Erkam

    rufus.oyuncak_sayisi()
    """  
    İste oyuncaklarimin Listesi:
    Kemik
    Top
    """