from Relationships.basic import db, Dog, app


# Tüm tabloları oluşturma
with app.app_context():

    db.drop_all() # Verileri tekrar tekrar eklemesin diye.
    db.create_all()


    # Row Oluşturma
    dog1 = Dog("Karabas", 3)
    dog2 = Dog("Mars", 4)

    # Tekli Veri Ekleme
    """  
    db.session.add(dog1)
    db.session.add(dog2)
    """

    # Çoklu Veri Ekleme
    db.session.add_all([dog1, dog2])

    print(dog1.id)
    print(dog2.id)
    # None
    # None


    # Commit

    db.session.commit()

    print(dog1.id)
    print(dog2.id)
    # 1
    # 2