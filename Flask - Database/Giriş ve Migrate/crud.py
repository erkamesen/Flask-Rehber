from basic import db, Dog, app


""" ## CREATE ## """

with app.app_context():
    my_dog = Dog("Rufus", 5)
    db.session.add(my_dog)
    db.session.commit()


""" ## READ ## """

with app.app_context():
    all_dogs = Dog.query.all() # Tüm köpekleri liste şeklinde getirir.
    print(all_dogs)

# ID ye göre Getirme

with app.app_context():
    dog1 = Dog.query.get(1)
    print(dog1.id)
    # 1
    print(dog1.name)
    # Karabas

# Filtreler

with app.app_context():
    mars = Dog.query.filter_by(name="Mars") # İsmi mars olan tüm köpeklkeri liste halinde getiricek.
    print(mars.all())
    # [Dog Mars is 4 year's old.]

    mars = Dog.query.filter_by(name="Mars").first()
    print(mars)
    # Dog Mars is 4 year's old.


""" ## UPDATE ## """

with app.app_context():
    dog1 = Dog.query.get(1)
    print(dog1.age)
    # 3
    dog1.age+=1
    print(dog1.age)
    # 4
    db.session.add(dog1)
    db.session.commit()


""" ## DELETE ## """

with app.app_context():
    all_dogs = Dog.query.all()
    print(all_dogs)
    
    dog2 = Dog.query.get(2)
    db.session.delete(dog2)
    db.session.commit()

    all_dogs = Dog.query.all()
    print(all_dogs)